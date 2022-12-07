from .file import File


class Directory:
    name: str = []
    parent: 'Directory' = None
    subdirectories: list['Directory'] = []
    files: list[File] = []

    def __init__(self, name, parent_directory: 'Directory'):
        self.name = name
        self.parent = parent_directory

    def add_directory(self, directory: 'Directory'):
        self.subdirectories.append(directory)

    def add_file(self, file: 'File'):
        self.files.append(file)

    def calculate_total_size(self) -> int:
        total_size: int = 0
        for file in self.files:
            total_size += file.size
        for subdirectory in self.subdirectories:
            total_size = + subdirectory.calculate_total_size()
        return total_size


class RootDirectory(Directory):
    def __init__(self, name):
        super().__init__(name, self)
