class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        length_dup = len(list(set(nums)))
        print(length_dup)
        print(length)

        if length_dup < length:
            return True
        else:
            return False
        