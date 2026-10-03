class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        unique = len(set(nums))

        if length != unique:
            return True 
        else:
            return False
        