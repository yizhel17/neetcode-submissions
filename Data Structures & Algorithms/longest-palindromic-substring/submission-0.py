class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        def is_p(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1

            return True
        
        res = ""
        maxL = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                if (j-i+1) > maxL:
                    if is_p(i, j):
                        maxL = j-i+1
                        res = s[i:j+1]
        
        return res
                