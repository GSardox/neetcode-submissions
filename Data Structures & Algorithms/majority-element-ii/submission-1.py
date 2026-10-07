class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        lim = len(nums) // 3
        result  = []

        seen = {}
        for i in nums:
            seen[i] = seen.get(i, 0) + 1
            if seen[i] > lim and i not in result:
                result.append(i)
        return(result)