class Solution:
    rucksack_contents: list[str] = []
    ASCII_OFFSET_LOWER = 97
    ASCII_OFFSET_UPPER = 65
    GAME_OFFSET_UPPER = 27
    GAME_OFFSET_LOWER = 1

    def __init__(self, input):
        self.rucksack_contents = input

    def solve(self) -> int:
        total_score = 0
        for rucksack in self.rucksack_contents:
            n = len(rucksack)
            mid = int(n/2)
            (l, r) = (rucksack[0:mid], rucksack[mid: n])
            assert (len(l) == len(r))
            (items_left, items_right) = (set(l), set(r))
            print(l)
            print(items_left)
            intersection = items_left.intersection(items_right)
            for item in intersection:
                if item.isupper():
                    total_score += ord(item) - self.ASCII_OFFSET_UPPER + self.GAME_OFFSET_UPPER
                if item.islower():
                    total_score += ord(item) - self.ASCII_OFFSET_LOWER + self.GAME_OFFSET_LOWER

        return total_score

def read_input() -> list[str]:
    input_file_name = 'input.txt'
    try:
        with open(input_file_name) as file:
            input_lines = file.readlines()
            if len(input_lines) == 0:
                raise Exception(f"File {input_file_name} is empty")
            input_lines_without_newline = [line.rstrip('\n') for line in input_lines]
            return input_lines_without_newline
    except EnvironmentError:
        raise Exception(f"File {input_file_name} is missing or invalid")


if __name__ == '__main__':
    input_lines = read_input()
    print(input_lines)
    solution = Solution(input_lines)
    print(f"Answer : {solution.solve()}")

