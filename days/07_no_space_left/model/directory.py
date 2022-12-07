from .file import File


class Directory:
    name: str = []
    parent: 'Directory' = None
    subdirectories: list['Directory'] = []
    files: list[File] = []

    def __init__(self, name, parent_directory: 'Directory'):
        self.name = name
        self.parent = parent_directory
        self.subdirectories = []
        self.files = []

    def add_directory(self, directory: 'Directory'):
        self.subdirectories.append(directory)

    def add_file(self, file: 'File'):
        self.files.append(file)

    def calculate_total_size(self) -> int:
        total_size: int = 0
        for file in self.files:
            total_size += file.size
        for subdirectory in self.subdirectories:
            # fuck you
            # total_size = + subdirectory.calculate_total_size()
            total_size += subdirectory.calculate_total_size()
        return total_size

    def subdirectory_exists(self, target_name: str) -> bool:
        for directory in self.subdirectories:
            if directory.name == target_name:
                return True
        return False

    def get_subdirectory_by_name(self, target_name: str):
        for directory in self.subdirectories:
            if directory.name == target_name:
                return directory
        raise Exception(f"Target subdirectory {target_name} of directory {self.name} does not exist")


class RootDirectory(Directory):
    def __init__(self, name):
        super().__init__(name, self)
