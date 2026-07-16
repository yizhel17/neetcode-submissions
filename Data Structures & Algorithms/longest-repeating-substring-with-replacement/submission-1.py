from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #update every time when we see a larger substring
        max_l = 0
        
        #hash map, track the times the element appears
        my_map = defaultdict(int)

        #Sliding window (left: slow, right: fast) --- Two pointers
        l = 0
        for r in range(len(s)):
            my_map[s[r]] += 1
            max_t = max(my_map.values())

            if (r-l+1) - max_t > k:
                my_map[s[l]] -= 1
                l += 1
            
            
            length = (r-l+1)
            max_l = max(max_l, length)
        
        return max_l