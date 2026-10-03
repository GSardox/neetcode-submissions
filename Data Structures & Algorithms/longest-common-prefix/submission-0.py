class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lst = []
        for i, letter in enumerate(strs[0]):
            for word in strs[1:]:
                if i >= len(word) or letter != word[i]:
                    return "".join(lst)
            lst.append(letter)
        return "".join(lst)