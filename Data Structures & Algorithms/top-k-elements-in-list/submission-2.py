import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        my_dict = collections.defaultdict(int)

        #collect the occurence
        for num in nums:
            my_dict[str(num)] += 1
        
        #heapify
        cur = []
        for val, ocr in my_dict.items():
            heapq.heappush(cur, (ocr, int(val)))

            while len(cur) > k:
                heapq.heappop(cur)
        
        for frq, nume in cur:
            ans.append(nume)
        
        return ans
