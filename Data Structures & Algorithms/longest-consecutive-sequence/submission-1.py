class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        unique = set(nums)
        seq_beg = []

        for num in unique:
            if num - 1 not in unique:
                seq_beg.append(num)

        longest = 0

        for beg in seq_beg:
            current = beg

            while current + 1 in unique:
                current += 1

            length = current - beg + 1

            if length > longest:
                longest = length

        return longest