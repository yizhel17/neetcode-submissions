class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        cur = []

        def dfs(i, total):
            if total == target:
                ans.append(cur[:])
                return
            if i >= len(candidates) or total > target:
                return
            

            cur.append(candidates[i])

            
            dfs(i+1, total + candidates[i])

            cur.pop()

            # skip candidates[i]
            # if skipping this value, skip ALL identical copies
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1

            dfs(i + 1, total)
        
        dfs(0, 0)

        return ans
