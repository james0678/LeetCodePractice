from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        total_max_freq = 0
        while len(s) > 0:
            res = Counter(s)
            max_char = max(res, key=res.get)  # Store the character with max frequency in max_char
            max_freq = res[max_char]  # Get the frequency of the max character

            if max_freq % 2 == 0:  # Even number frequency
                result += max_freq
                s = ''.join([char for char in s if char != max_char])  # Remove all occurrences of max_char
                total_max_freq = max_freq
            else:  # Odd number frequency
                if max_freq == 1 and total_max_freq == 1:
                    result = 1
                else:
                    result += max_freq - 1
                    s = ''.join([char for char in s if char != max_char])  # Remove all occurrences of max_char
                    total_max_freq = max_freq

        return result