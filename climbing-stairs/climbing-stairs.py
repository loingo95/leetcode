class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
#         since we can step 1 or 2 steps to reach n, so we will find the way to reach n-1 and n-2 stars,
        def recur_climb_stairs(nrof_stairs):
            if nrof_stairs == 1:
                return 1
            elif nrof_stairs == 2:
                return 2
            
            if nrof_stairs in cache:
                nrof_ways = cache[nrof_stairs]
            else:
                nrof_ways = recur_climb_stairs(nrof_stairs-1) + recur_climb_stairs(nrof_stairs-2)
                cache[nrof_stairs] = nrof_ways
            
            return nrof_ways
        
        return recur_climb_stairs(n)