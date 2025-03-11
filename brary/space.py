from .location import *
from .essentials import *

class ColorObject:
    def __init__(self, color: str) -> None:
        color = "LIGHTBLACK_EX" if color.lower() in ["grey", "gray"] else color
        self.color: str = getattr(Fore, color.upper())
    def apply(self, string: str) -> str:
        return f"{self.color}{string}{Style.RESET_ALL}"
class _ColorClass:
    def __getattr__(self, item: str) -> ColorObject:
        return ColorObject(item)
Color: _ColorClass = _ColorClass()
class TileTexture:
    def __init__(self, texture: str, color: ColorObject) -> None:
        if len(texture) > 1:
            raise ValueError("texture must be only 1 character.")
        self.texture: str = str(texture)
        self.color: ColorObject = color
    def __str__(self, color: bool = True) -> str:
        return self.color.apply(self.texture) if color else self.texture
class BoardState:
    def __init__(self, space_id: int, location: LocationArray, texture: TileTexture, tag: str) -> None:
        self.space_id: int = space_id
        self.location: LocationArray = location
        self.texture: TileTexture = texture
        self.tag: str = tag
    def __str__(self) -> str:
        return f"{self.space_id} ({self.texture}) at {self.location} with tag '{self.tag}'"
    @staticmethod
    def compare(state1: "BoardState", state2: "BoardState") -> bool:
        return str(state1) == str(state2)
class Piston:
    def __init__(self, board: "Board") -> None:
        self.board: "Board" = board
        self.pushes: int = 0
    def push(self, space_id: int, key_or_offset: str | LocationOffset, distance: int = 1) -> None:
        for _ in range(distance):
            offset: LocationOffset = key_or_offset if isinstance(key_or_offset, LocationOffset) else LocationOffset.generate(key_or_offset)
            old_location: LocationArray = self.board.location_by_id(space_id)
            new_location: LocationArray = offset.apply(old_location)
            self.board.StatePlacementOperator.ensure_location(self.board, new_location)
            self.board.StatePlacementOperator(
                self.board,
                space_id,
                new_location,
                self.board.tag_by_id(space_id),
                self.board.texture_by_id(space_id)
            )
            self.board.rm_by_id(space_id)
            self.pushes += 1