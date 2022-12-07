from .file import File
from .directory import Directory, RootDirectory


class DiskStructureParser:
    CMD_PREFIX = "$"
    DIR_PREFIX = "dir"

    LIST_DIRECTORY_CMD = "ls"
    CHANGE_DIRECTORY_CMD = "cd"

    ROOT_DIRECTORY_NAME = "/"
    PARENT_DIRECTORY_NAME = ".."

    END_OF_INPUT = -1

    def create_file_system_structure_from_console_lines(self, console_lines: list[str]) -> Directory:
        root_directory = RootDirectory(self.ROOT_DIRECTORY_NAME)
        current_directory = root_directory
        for line_idx in range(0, len(console_lines)):
            line = console_lines[line_idx]
            match line.split():
                case [self.CMD_PREFIX, self.CHANGE_DIRECTORY_CMD, self.ROOT_DIRECTORY_NAME]:
                    # cd /
                    current_directory = root_directory
                case [self.CMD_PREFIX, self.CHANGE_DIRECTORY_CMD, self.PARENT_DIRECTORY_NAME]:
                    # cd ..
                    current_directory = current_directory.parent
                case [self.CMD_PREFIX, self.CHANGE_DIRECTORY_CMD, directory_name]:
                    # cd name
                    if current_directory.subdirectory_exists(directory_name):
                        current_directory = current_directory.get_subdirectory_by_name(directory_name)
                    else:
                        new_directory = Directory(directory_name, current_directory)
                        current_directory = new_directory
                case [self.CMD_PREFIX, self.LIST_DIRECTORY_CMD]:
                    # $ ls -> lines until next $* contain directory structure
                    next_line_idx = line_idx + 1
                    index_of_next_command = self.find_index_of_next_command(next_line_idx, console_lines)
                    if index_of_next_command == self.END_OF_INPUT:
                        lines_with_directory_structure = console_lines[next_line_idx:]
                        self.create_directory_structure(current_directory, lines_with_directory_structure)
                        return root_directory
                    else:
                        lines_with_directory_structure = console_lines[next_line_idx:index_of_next_command - 1]
                        self.create_directory_structure(current_directory, lines_with_directory_structure)
                case [_, _]:
                    continue
        return root_directory

    def find_index_of_next_command(self, start_idx: int, console_lines: list[str]) -> int:
        for line_idx in range(start_idx, len(console_lines)):
            line = console_lines[line_idx]
            match line.split():
                case [self.CMD_PREFIX, _]:
                    return line_idx
        return self.END_OF_INPUT

    def create_directory_structure(self, current_directory, lines_with_directory_structure):
        # lines with directories and filenames
        # dir dirname
        # size filename
        for line in lines_with_directory_structure:
            match line.split():
                case [self.DIR_PREFIX, directory_name]:
                    current_directory.add_directory(Directory(directory_name, current_directory))
                case [file_size, file_name]:
                    current_directory.add_file(File(file_name, int(file_size)))
