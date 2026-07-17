class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #解法一
        numSet = set(nums)
        longest = 0

        for num in numSet:

            # 不是起点
            if num - 1 in numSet:
                continue
            
            #是起点
            length = 1

            while num + 1 in numSet:
                num += 1
                length += 1

            longest = max(longest, length)

        return longest