class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        seen = {0: 1}
        res = 0
        sums = 0

        for n in nums:
            sums += n

            if sums - k in seen:
                res += seen[sums - k]

            seen[sums] = seen.get(sums, 0) + 1

        return res