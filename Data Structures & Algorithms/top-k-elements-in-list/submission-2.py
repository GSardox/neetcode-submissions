class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = {}
        lst  = []

        sol = []

        for  i in nums:
            seen[i] = seen.get(i, 0  ) + 1
        
        for num, cnt in seen.items():
            lst.append([cnt, num])
        lst.sort()

        while len(sol) < k:
            sol.append(lst.pop()[1])
        return sol 

    

        #ordered = sorted(seen, key=seen.get, reverse=True)
        #lst.appe