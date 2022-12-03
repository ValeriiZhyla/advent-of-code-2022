class PrioritizationRules:
    ASCII_OFFSET_LOWER = 97
    ASCII_OFFSET_UPPER = 65
    GAME_OFFSET_UPPER = 27
    GAME_OFFSET_LOWER = 1

    def priority_of_set(self, letters: set[str]) -> int:
        score = 0
        for item in letters:
            if item.isupper():
                score += ord(item) - self.ASCII_OFFSET_UPPER + self.GAME_OFFSET_UPPER
            if item.islower():
                score += ord(item) - self.ASCII_OFFSET_LOWER + self.GAME_OFFSET_LOWER
        return score
