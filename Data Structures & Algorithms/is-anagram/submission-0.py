class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occ1 = defaultdict(int)
        occ2 = defaultdict(int)
        
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                occ1[s[i]] += 1
                occ2[t[i]] += 1
        
        return occ1 == occ2