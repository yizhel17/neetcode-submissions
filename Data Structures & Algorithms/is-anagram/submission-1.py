from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_d = defaultdict(int)

        for let in s:
            s_d[let] += 1
        
        for cha in t:
            if cha not in s_d:
                return False
            else:
                s_d[cha] -= 1
        
        return set([num for num in s_d.values()]) == set([0])
        