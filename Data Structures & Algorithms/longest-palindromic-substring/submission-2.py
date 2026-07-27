class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Solution 1: Burte force: O(N^3)
        # if len(s) < 2:
        #     return s
        
        # def is_p(l, r):
        #     while l < r:
        #         if s[l] != s[r]:
        #             return False
        #         l+=1
        #         r-=1

        #     return True
        
        # res = ""
        # maxL = 0

        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if (j-i+1) > maxL:
        #             if is_p(i, j):
        #                 maxL = j-i+1
        #                 res = s[i:j+1]
        
        # return res

        
        #Solution 2: Expand around center
        maxL = 0
        ans = ""

        for i in range(len(s)):
            
            #odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxL:
                    ans = s[l: r+1]
                    maxL = r-l+1
                l -= 1
                r += 1
            
            #even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxL:
                    ans = s[l : r + 1]
                    maxL = r - l + 1
                l -= 1
                r += 1
            
        return ans