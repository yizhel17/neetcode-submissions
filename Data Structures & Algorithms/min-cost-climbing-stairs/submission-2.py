class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #we can just need the min cost of the next one/two step
        #we only need to reverse our thinking, and take the minimum of the cost[0] and the cost[1] at the end

        # The cheapest way to climb from this current step is its own cost, 
        # PLUS the minimum of the two steps directly in front of it!
        #we start from the last third element
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2]) #make a choice either choose 1 step or 2 steps at a time

        #finally, return the base case at index 0/1
        return min(cost[0], cost[1])