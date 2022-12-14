class File:
    def __init__(self, size: int, name: str):
        self.size: int = size
        self.name: str = name

    def __str__(self) -> str:
        return f"{self.name} size:({self.size})"