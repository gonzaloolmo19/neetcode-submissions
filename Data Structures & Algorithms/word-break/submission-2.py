class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # wordDict = set(wordDict)
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                if i - len(word) >= 0:
                    print(s[i-len(word)+1: i+1])
                    if s[i-len(word)+1: i+1] == word:
                        dp[i] = dp [i-len(word)]
                        if dp[i] == True:
                            break
                else:
                    if s[i-len(word)+1: i+1] == word:
                        dp[i] = True
            print(dp)
            
        return dp[-1]
            
        