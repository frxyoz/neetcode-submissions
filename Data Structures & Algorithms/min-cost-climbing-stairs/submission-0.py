class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost[0], cost[1])
        costs = [float('inf')] * (len(cost) + 1)
        costs[0], costs[1] = 0, 0
        for i in range(2, len(cost) + 1):
            costs[i] = min(costs[i-2] + cost[i-2], costs[i-1] + cost[i-1])
        print(costs)
        return costs[len(cost)]