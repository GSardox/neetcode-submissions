class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value → index

        for i, num in enumerate(nums):
            complement = target - num  # what do we need?
            if complement in seen:
                return [seen[complement], i]  # found it
            seen[num] = i  # store current number and its index