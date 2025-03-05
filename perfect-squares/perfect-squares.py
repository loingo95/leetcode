class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        import math
        from collections import deque
        
        # this is a BFS problem with graph construct from nodes are perfect square number that < n,
        # edges of each node are it self to all available perfect squared
        # we loop through each iterations, the number of iterations is the least number of perfect square numbers 
        
        
        queue = deque()
        available_perfect_squares = [i*i for i in range(1, int(math.sqrt(n)) + 1)]
        steps = 0
        print(available_perfect_squares)
        
        # root is 0
        queue.append(0)
        
        while queue:
            next_nodes = []
            while queue:
                node = queue.popleft()
                if node == n:
                    return steps
                next_nodes.extend([node+ps for ps in available_perfect_squares])
                
            queue.extend(set(next_nodes))
            steps += 1
                
        