class CommunicationDevice:
    original_signal: str = ""

    LENGTH_OF_START_MARKER: int = 4
    LENGTH_OF_MESSAGE_MARKER: int = 14

    def __init__(self, signal):
        self.original_signal = signal

    def find_start_of_packet(self):
        return self.find_first_index_after_marker(self.LENGTH_OF_START_MARKER)

    def find_start_of_message(self):
        return self.find_first_index_after_marker(self.LENGTH_OF_MESSAGE_MARKER)

    def find_first_index_after_marker(self, length_of_marker: int) -> int:
        for start_of_potential_marker in range(0, len(self.original_signal) - length_of_marker):
            end_of_potential_marker = start_of_potential_marker + length_of_marker
            potential_marker = self.original_signal[start_of_potential_marker:end_of_potential_marker]
            potential_marker_characters = set(potential_marker)
            if len(potential_marker) == len(potential_marker_characters):
                return end_of_potential_marker
