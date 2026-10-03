class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        

        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1
            majority = len(nums) // 2
            if  seen[num] > majority:
                return num
        


        