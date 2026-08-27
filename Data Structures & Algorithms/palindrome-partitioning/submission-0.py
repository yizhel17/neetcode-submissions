class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        cur = []

        def isP(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
            
                left += 1
                right -= 1
            
            return True
        
        def bck(start):
            if start == len(s):
                ans.append(cur[:])
                return
            

            for end in range(start, len(s)):
                if isP(start, end):
                    cur.append(s[start: end + 1])

                    bck(end + 1)

                    cur.pop()
            
        bck(0)

        return ans
