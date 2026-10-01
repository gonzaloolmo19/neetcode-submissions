class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Transform string to be valid
        s = s.lower()
        
        t= ""
        for l in range(len(s)):
            if ord('a')<=ord(s[l]) and ord(s[l])<=ord('z') or ord('0') <= ord(s[l]) <= ord('9'):
                t += s[l]

        # Check palindrome
        i = 0
        j = len(t)-1
        while i < j:
            if t[i] != t[j]:
                return False
            i += 1
            j -= 1
        
        return True
        