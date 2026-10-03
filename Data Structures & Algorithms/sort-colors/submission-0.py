class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for _ in range(len(nums)):
            for idx in range(len(nums) - 1):
                if nums[idx] > nums[idx + 1]:
                    nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]