# Created by Leon Hunter at 3:57 PM 10/23/2020
class StringManipulator(object):
    def get_hello_world(self):
        return ("Hello, World") # TODO - Implement solution

    def concatenate(self, value_to_be_added_to, value_to_add):
        return str(value_to_be_added_to + str(value_to_add) # TODO - Implement solution

    def substring_inclusive(self, string_to_fetch_from, starting_index, ending_index):
        string_to_fetch_from = str(string_to_fetch_from)
        startIndex = int(starting_index)
        endingIndex = int(ending_index) + 1
        resultInclusive = string_to_fetch_from[startIndex:endingIndex]
        return resultInclusive # TODO - Implement solution

    def substring_exclusive(self, string_to_fetch_from, starting_index, ending_index):
        string_to_fetch_from = str(string_to_fetch_from)
        startIndex = int(starting_index) + 1
        endingIndex = int(ending_index)
        resultInclusive = string_to_fetch_from[startIndex:endingIndex]
        return resultInclusive # TODO - Implement solution

    def compare(self, first_value, second_value):
        if first_value == second_value
            return true
        else
            return false # TODO - Implement solution

    def get_middle_character(self, string_to_fetch_from):
        return string_to_fetch_from[len(string_to_fetch_from / 2)] # TODO - Implement solution

    def get_first_word(self, string_to_fetch_from):
        return string_to_fetch_from()[0] # TODO - Implement solution

    def get_second_word(self, string_to_fetch_from):
        return string_to_fetch_from()[1] # TODO - Implement solution

    def reverse(self, string_to_be_reversed):
        return string_to_be_reversed[::-1] # TODO - Implement solution