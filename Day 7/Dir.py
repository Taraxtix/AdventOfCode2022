from File import File


class Dir:
    def __init__(self, name: str, parent):
        self.parent: Dir = parent
        self.name: str = name
        self.dirs: list[Dir] = []
        self.files: list[File] = []

    def add_file(self, description: list[str]):
        self.files.append(File(int(description[0]), description[1]))

    def add_dir(self, name: str):
        self.dirs.append(Dir(name, self))

    def found_dir_by_name(self, name: str):
        for dir in self.dirs:
            if dir.name == name:
                return dir

    def get_total_size(self) -> int:
        size = 0
        for file in self.files:
            size += file.size
        for dir in self.dirs:
            size += dir.get_total_size()
        return size

    def __str__(self) -> str:
        if self.parent is None:
            return self.name
        if self.parent.name == "/":
            return self.name
        return f"{self.parent}/{self.name}"
