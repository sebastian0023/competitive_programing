def minCostClimbingStairs( cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        for i in range(len(cost)-3,-1,-1):
            cost[i] += min(cost[i+1],cost[i+2])
            print("Cost at step", i, ":", cost[i])
        return min(cost[0],cost[1])

cost = [10, 15, 20]

minCost = minCostClimbingStairs(cost)
print("Minimum cost to reach the top of the stairs:", minCost)