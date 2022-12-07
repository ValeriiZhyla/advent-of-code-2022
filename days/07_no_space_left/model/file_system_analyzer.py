import itertools

from .directory import Directory


class FileSystemAnalyzer:
    def get_total_size_of_directories_with_size_less_or_equal_than(self, start_directory: Directory, size_threshold: int) -> int:
        directories = self.find_all_directories_with_total_size_less_than_threshold(start_directory, size_threshold)
        return sum(map(lambda directory: directory.calculate_total_size(), directories))

    def find_all_directories_with_total_size_less_than_threshold(self, directory, size_threshold):
        return self.find_all_directories_with_total_size_less_than_threshold_acc(directory, size_threshold, [])

    def find_all_directories_with_total_size_less_than_threshold_acc(self, directory, size_threshold, accumulator):
        if directory.calculate_total_size() <= size_threshold:
            accumulator.append(directory)
        for subdir in directory.subdirectories:
            accumulator.extend(self.find_all_directories_with_total_size_less_than_threshold_acc(subdir, size_threshold, []))
        return accumulator
