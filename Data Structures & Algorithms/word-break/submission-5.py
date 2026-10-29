class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # wordDict = set(wordDict)
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)+1):
            for word in wordDict:
                if i - len(word) >= 0 and dp[i-len(word)]:
                    if s[i-len(word): i] == word:
                        dp[i] = True
                        break
            
        return dp[-1]
            
        