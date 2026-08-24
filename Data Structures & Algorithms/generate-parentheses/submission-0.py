class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(res, open_p, close_p):
            #base case (返回完整答案)
            if open_p == n and close_p == n:
                ans.append(res)
                return
            
            if open_p < n:
                backtrack(res + "(", open_p + 1, close_p)
            
            if close_p < open_p:
                backtrack(res + ")", open_p, close_p + 1)
        
        backtrack("", 0, 0)

        return ans
