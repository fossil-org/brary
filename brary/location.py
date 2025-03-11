class _Location:
    SIGN = ""
    def __init__(self, value: int) -> None:
        self.value: int = value
    def __int__(self) -> int:
        return self.value
    def __str__(self) -> str:
        return f"{self.SIGN}{self.value}"
class LocationX(_Location):
    SIGN = "x"
class LocationY(_Location):
    SIGN = "y"
class LocationArray:
    def __init__(self, x: LocationX, y: LocationY) -> None:
        self.x: LocationX = x
        self.y: LocationY = y
    def __iter__(self) -> iter:
        return iter([self.x, self.y])
    def __str__(self) -> str:
        return f"{self.x}{self.y}"
    @staticmethod
    def compare(location1: "LocationArray", location2: "LocationArray") -> bool:
        return str(location1) == str(location2)
    @classmethod
    def from_int(cls, x: int, y: int) -> "LocationArray":
        return cls(LocationX(x), LocationY(y))
class LocationOffset:
    def __init__(self, x_offset: LocationX, y_offset: LocationY) -> None:
        self.x: LocationX = x_offset
        self.y: LocationY = y_offset
    @classmethod
    def generate(cls, key: str) -> "LocationOffset":
        return cls(LocationX({
            "q": -1, "w": +0, "e": +1,
            "a": -1, "s": +0, "d": +1,
            "z": -1, "x": +0, "c": +1
        }[key]), LocationY({
            "q": +1, "w": +1, "e": +1,
            "a": +0, "s": -1, "d": +0,
            "z": -1, "x": -1, "c": -1
        }[key]))
    def apply(self, location: LocationArray) -> LocationArray:
        return LocationArray(
            LocationX(
                int(location.x) + int(self.x)
            ),
            LocationY(
                int(location.y) + int(self.y)
            )
        )