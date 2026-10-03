class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        counts_t = {}

        if len(s) != len(t):
            return False

        for char in s:
            counts[char] = counts.get(char, 0) + 1

        for char_2 in t:
            counts_t[char_2] = counts_t.get(char_2, 0) + 1

        # compare once both are fully built
        if counts == counts_t:
            return True
        else:
            return False