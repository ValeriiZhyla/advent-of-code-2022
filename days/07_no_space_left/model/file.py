class File:
    name: str = ""
    size: int = 0

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
