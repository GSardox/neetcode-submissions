class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        counts_t = {}

        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i],0) + 1
        for j in range(len(t)):
            counts_t[t[j]] = counts_t.get(t[j],0) + 1
        
        if  counts != counts_t:
            return False 
        else:
            return True 
