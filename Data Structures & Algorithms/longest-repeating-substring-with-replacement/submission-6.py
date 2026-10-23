from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        freq = defaultdict(int)
        left = 0
        max_f = 0

        for right in range(len(s)):
            freq[s[right]] += 1

            max_f = max(max_f, freq[s[right]])

            while (right - left + 1) - max_f > k:
                freq[s[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans
