class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1

        cur_small = 1

        while cur_small in nums:
            cur_small += 1

        return cur_small