class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        if len(s) == 0:
            return 0

        l = 0
        r = 0
        win_cnt = defaultdict(int)
        win_cnt[s[0]] += 1
        duplicates = 0

        while r < len(s) - 1:
            r += 1
            win_cnt[s[r]] += 1
            if win_cnt[s[r]] == 2:
                duplicates += 1

            if duplicates > 0:
                if win_cnt[s[l]] == 2:
                    duplicates -= 1
                win_cnt[s[l]] -= 1
                l += 1
        
        return r-l + 1


        