# Given a string, find the length of the longest substring in it with no more
# than K distinct characters.
import unittest


# Example 1:
# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters
# is "araa".

# Example 2:
# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters
# is "aa".

# Example 3:
# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters
# are "cbbeb" & "bbebi".

def longest_substr_with_k_distinct(k, str):
    start = 0
    chars = {}
    max_len = 0

    for end in range(len(str)):
        count = chars.setdefault(str[end], 1)
        if count > 1:
            chars[str[end]] = count + 1

        while len(chars) > k:
            chars[str[start]] -= 1
            # NOTE: WRONG PLACE!!! we could be deleting the wrong char,
            #   i.e. the next int the str
            # start += 1
            if chars[str[start]] == 0:
                del chars[str[start]]
            start += 1

        # NOTE: here always going to be valid, len(chars) == k
        #   so we dont need to add that condition
        max_len = max(max_len, end - start + 1)

    return max_len

class TestLongestSubstrWithKDistinct(unittest.TestCase):
    def test_longest_substr_with_k_distinct(self):
        self.assertEqual(4, longest_substr_with_k_distinct(2, 'araaci'))

    def test_longest_substr_with_k_distinct2(self):
        self.assertEqual(2, longest_substr_with_k_distinct(1, 'araaci'))

    def test_longest_substr_with_k_distinct3(self):
        self.assertEqual(5, longest_substr_with_k_distinct(3, 'cbbebi'))

