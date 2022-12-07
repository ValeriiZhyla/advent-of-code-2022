import itertools

from .directory import Directory


class FileSystemAnalyzer:
    def get_total_size_of_directories_with_size_less_or_equal_than(self, start_directory: Directory, size_threshold: int) -> int:
        directories = self.find_all_directories_with_total_size_less_than_threshold(start_directory, size_threshold)
        return sum(map(lambda directory: directory.calculate_total_size(), directories))


    def get_size_of_smallest_directory_to_delete_for_update(self, root_directory: Directory, total_space: int, required_space: int) -> int:
        total_space_used = root_directory.calculate_total_size()
        total_space_free = total_space - total_space_used
        space_to_clean = required_space - total_space_free
        all_directories_sorted_by_size_desc = self.get_directories_sorted_by_size_desc(root_directory)
        for dir_idx in range(0, len(all_directories_sorted_by_size_desc)-1):
            current_dir = all_directories_sorted_by_size_desc[dir_idx]
            next_dir = all_directories_sorted_by_size_desc[dir_idx + 1]
            if current_dir.calculate_total_size() >= space_to_clean > next_dir.calculate_total_size():
                return current_dir.calculate_total_size()
            elif next_dir.calculate_total_size() > space_to_clean:
                continue
            else:
                raise Exception("There is no directory, that can be deleted to free up space")

    def find_all_directories_with_total_size_less_than_threshold(self, directory: Directory, size_threshold: int) -> list[Directory]:
        return self.find_all_directories_with_total_size_less_than_threshold_acc(directory, size_threshold, [])

    def find_all_directories_with_total_size_less_than_threshold_acc(self, directory: Directory, size_threshold: int, accumulator: list[Directory])-> list[Directory]:
        if directory.calculate_total_size() <= size_threshold:
            accumulator.append(directory)
        for subdir in directory.subdirectories:
            accumulator.extend(self.find_all_directories_with_total_size_less_than_threshold_acc(subdir, size_threshold, []))
        return accumulator

    def get_directories_sorted_by_size_desc(self, root: Directory) -> list[Directory]:
        all_directories = self.get_all_directories_as_plain_list(root, [])
        sorted_directories = sorted(all_directories, key=lambda d: d.calculate_total_size(), reverse=True)
        return sorted_directories

    def get_all_directories_as_plain_list(self, directory: Directory, accumulator: list[Directory]) -> list[Directory]:
        accumulator.append(directory)
        for subdir in directory.subdirectories:
            accumulator.extend(self.get_all_directories_as_plain_list(subdir, []))
        return accumulator

