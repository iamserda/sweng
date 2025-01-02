from tests import main
"""Module to run unit tests for code."""


def longest_common_prefix(string_list: list[str]) -> str:
    """ TODO: Write a description for this function. """
    if not string_list:
        return ""
    if len(string_list) == 1:
        return string_list[0]

    def compare_two_string(str1: str, str2: str) -> str:
        """ Compares two strings, returns a substring that's common between str1 and str2"""
        temp_lcp = []
        shortest_str = str1 if len(str1) < len(str2) else str2
        for index in range(len(shortest_str)):
            if str1[index] != str2[index]:
                break
            temp_lcp.append(str1[index])
        return "".join(temp_lcp)
    idx1 = 0
    lcp_found = ""
    str1 = string_list[idx1]
    str2 = string_list[idx1 + 1]
    lcp_found = compare_two_string(str1, str2)
    for idx in range(2, len(string_list)):
        lcp_found = compare_two_string(string_list[idx], lcp_found)
    return lcp_found


"""TESTS ARENA:"""


class TestLongestCommonPrefix(unittest.TestCase):

    def test_basic_functionality(self):
        self.assertEqual(longest_common_prefix(
            ["flower", "flow", "flight"]), "fl")
        self.assertEqual(longest_common_prefix(["dog", "racecar", "car"]), "")

    def test_empty_list(self):
        self.assertEqual(longest_common_prefix([]), "")

    def test_single_string(self):
        self.assertEqual(longest_common_prefix(["alone"]), "alone")

    def test_no_common_prefix(self):
        self.assertEqual(longest_common_prefix(["abc", "def", "ghi"]), "")

    def test_varied_length_strings(self):
        self.assertEqual(longest_common_prefix(["a", "ab", "abc"]), "a")
        self.assertEqual(longest_common_prefix(
            ["longest", "longer", "long"]), "long")


if __name__ == "__main__":
    main.unittest.main()
