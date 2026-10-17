class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        for i in range(n+1):
            bit = 1
            cnt = 0
            for j in range(11):
                if i & bit:
                    cnt +=1
                bit = bit << 1
            
            res[i] = cnt
        
        return res
            