class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        
        max_f = max(count)
        max_count = 0
        for f in count:
            if f == max_f:
                max_count += 1
        
        time = (max_f - 1) * (n + 1) + max_count
        return max(len(tasks), time)
