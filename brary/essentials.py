import os, random, time

from pathlib import Path
from typing import Any, Literal, Callable
from colorama import Style, Fore

from .location import *
from .space import *
class GamePlayerManager:
    def __init__(self) -> None:
        ...
    def add_class(self, cls: type):
        self.__dict__ |= {
            f"{cls.__name__.capitalize()}Class": cls,
            cls.__name__.lower(): cls()
        }
    @classmethod
    def setup(cls) -> "GamePlayerManager":
        gpm: GamePlayerManager = cls()
        gpm.add_class(GamePlayerManager.create_class("Board"))
        return gpm
    @staticmethod
    def create_class_from_str(name: str, s: str) -> type:
        s = "..." if not s else s
        lns: list[str] = f"""
from brary import *
class {name}:
    def __getattr__(self, name: str) -> None:
        raise AttributeError(f"attempted to retrieve {name} attribute '{{name}}', but it is not defined in the {name} script.")
        """.strip().split("\n") + [f"    {ln}" for ln in s.split("\n")]
        s = "\n".join(lns)
        exec(s)
        return locals()[name]
    @staticmethod
    def create_class(name: str) -> type:
        scripts_path: Path = Path(os.getcwd()) / "scripts"
        file_path: Path = scripts_path / name
        if not scripts_path.exists():
            raise FileNotFoundError(
                f"gpm setup() requires a scripts directory in your current working directory ({os.getcwd()}). you can run 'mkdir {scripts_path}' to create it.")
        if not file_path.exists():
            raise FileNotFoundError(f"gpm setup() requires {name} script in {scripts_path}")
        with file_path.open() as file:
            code: str = file.read()
        return GamePlayerManager.create_class_from_str(name, code)
class Game:
    def __init__(self, board: "Board") -> None:
        self.board: "Board" = board
        self.player: object = GamePlayerManager.create_class("Player")
        self.piston: Piston = board.new(Piston)
    def loop(self, until: Callable | bool, player_tag: str = "Player") -> None:
        while not (until() if callable(until) else until):
            os.system("cls" if os.name == "nt" else "clear")
            print(self.board.render())
            try:
                q: str = input("> ")
            except (KeyboardInterrupt, EOFError):
                return
            if q in list("qweasdzxc"):
                pushes_before: int = self.piston.pushes
                try:
                    self.piston.push(self.board.id_by_tag(player_tag), q, self.player.S)
                except ValueError:
                    pushes_after: int = self.piston.pushes
                    elapsed_pushes: int = pushes_after - pushes_before
                    if elapsed_pushes == 0:
                        print(f"{Fore.RED}Cannot go there!{Style.RESET_ALL}")
                        time.sleep(0.4)
class Board:
    def __init__(self, size: LocationArray, bg: TileTexture) -> None:
        self.size: LocationArray = size
        self.states: list[BoardState] = []
        self.bg: TileTexture = bg
    @classmethod
    def setup(cls) -> "Board":
        gpm: GamePlayerManager = GamePlayerManager.setup()
        board: gpm.BoardClass = gpm.board
        return cls(LocationArray(LocationX(board.W), LocationY(board.H)), TileTexture(board.T, ColorObject(board.C)))
    @staticmethod
    def generate_random_space_id() -> int:
        return random.randint(0, 999999)
    def new(self, cls: type) -> Any:
        return cls(self)
    def state_taken(self, location: LocationArray) -> bool:
        for state in self.states:
            if LocationArray.compare(state.location, location):
                return state
        return False
    class StatePlacementOperator:
        def __init__(
            self,
            board: "Board",
            space_id: int,
            location: LocationArray,
            tag: str,
            texture: TileTexture,
            override: bool = True
        ) -> None:
            self.board: "Board" = board
            self.ensure_location(board, location)
            state: BoardState | False = board.state_taken(location)
            if not override and state is not False:
                raise ValueError(f"location {location} already taken.")
            for i, state2 in enumerate(board.states):
                if BoardState.compare(state, state2):
                    board.states.pop(i)
            board.states.append(BoardState(space_id, location, texture, tag))
            self.__state: BoardState = board.states[-1]
        def fetch(self) -> BoardState:
            return self.__state
        @staticmethod
        def validate_location(board: "Board", location: LocationArray) -> bool | str:
            return not any([
                int(location.x) > int(board.size.x),
                int(location.y) > int(board.size.y),
                int(location.x) <= 0,
                int(location.y) <= 0
            ])
        @staticmethod
        def ensure_location(board: "Board", location: LocationArray) -> None:
            if not Board.StatePlacementOperator.validate_location(board, location):
                raise ValueError(f"location {location} is out of bounds.")
    def _look_for(self, formula: str, **vars: Any) -> Any:
        for i, state in enumerate(self.states):
            if eval(formula, globals() | locals() | vars, {}):
                return i, state
        return 0, None

    def rm_by_state(self, state: BoardState) -> None:
        i, state = self._look_for(f"state.space_id == space_id", space_id=state.space_id)
        if state is None:
            raise ValueError(f"tile with id '{space_id}' not found.")
        self.states.pop(i)

    # by id:

    def state_by_id(self, space_id: int) -> BoardState:
        return self._look_for(f"state.space_id == space_id", space_id=space_id)[1]
    def location_by_id(self, space_id: int) -> LocationArray:
        return self.state_by_id(space_id).location
    def tag_by_id(self, space_id: int) -> LocationArray:
        return self.state_by_id(space_id).tag
    def texture_by_id(self, space_id: int) -> LocationArray:
        return self.state_by_id(space_id).texture
    def rm_by_id(self, space_id: int) -> None:
        self.rm_by_state(self.state_by_id(space_id))

    # by tag:

    def state_by_tag(self, tag: str) -> BoardState:
        return self._look_for(f"state.tag == tag", tag=tag)[1]
    def location_by_tag(self, tag: str) -> LocationArray:
        return self.state_by_tag(tag).location
    def id_by_tag(self, tag: str) -> int:
        return self.state_by_tag(tag).space_id
    def texture_by_tag(self, tag: str) -> LocationArray:
        return self.state_by_tag(tag).texture
    def rm_by_tag(self, tag: str) -> None:
        self.rm_by_state(self.state_by_tag(tag))

    # by location:

    def state_by_location(self, location: LocationArray) -> BoardState:
        return self._look_for(f"LocationArray.compare(state.location, location)", location=location)[1]
    def id_by_location(self, location: LocationArray) -> int:
        return self.state_by_location(location).space_id
    def tag_by_location(self, location: LocationArray) -> str:
        return self.state_by_location(location).tag
    def texture_by_location(self, location: LocationArray) -> LocationArray:
        return self.state_by_location(location).texture
    def rm_by_location(self, location: LocationArray) -> None:
        self.rm_by_state(self.state_by_location(location))

    def create(self, tag: str, name: str | None = None) -> object:
        """name parameter defaults to tag"""
        name = tag if name is None else name
        space_cls: type = GamePlayerManager.create_class(name)
        space_id: int = self.generate_random_space_id()
        class new_space_cls(space_cls):
            id = space_id
            def rm(self1):
                self.rm_by_id(space_id)
        space: space_cls = new_space_cls()
        location_x: int = space.X
        location_y: int = space.Y
        texture: str = space.T
        color: str | ColorObject = space.C
        self.StatePlacementOperator(
            self,
            space_id,
            LocationArray(
                LocationX(location_x),
                LocationY(location_y)
            ),
            tag,
            TileTexture(
                texture,
                ColorObject(color) if isinstance(color, str) else color
            )
        )
        return space
    def render(self) -> str:
        lns = []
        for y in range(-int(self.size.y), 0):
            ln = [
                str(self.bg)
                if not self.state_taken(LocationArray.from_int(x, -y))
                else str(self.state_taken(LocationArray.from_int(x, -y)).texture)
                for x in range(1, int(self.size.x) + 1)
            ]
            lns.append("".join(ln))
        return "\n".join(lns)