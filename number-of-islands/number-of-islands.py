class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        from collections import deque
        
        nrof_islands = 0

        def neighbor_lands(row_idx, col_idx, m, n):
            possible_coords = [
                (row_idx-1, col_idx),
                (row_idx+1, col_idx),
                (row_idx, col_idx-1),
                (row_idx, col_idx+1)
            ]

            neighbor_coords = []
            for row_idx, col_idx in possible_coords:
                if row_idx>=0 and row_idx<m and col_idx>=0 and col_idx<n and grid[row_idx][col_idx] == "1":
                    neighbor_coords.append((row_idx, col_idx))
            return neighbor_coords


        m = len(grid)
        n = len(grid[0])
        visited = set()
        _queue = deque()

        for row_idx in range(m):
            for col_idx in range(n):
                current_node = (row_idx, col_idx)
                if current_node in visited or grid[row_idx][col_idx] != "1":
                    continue

                nrof_islands += 1       
                _queue.append(current_node)
                while _queue:
                    current_node = _queue.popleft()
                    if current_node in visited:
                        continue
                    visited.add(current_node)
                    neighbors = neighbor_lands(current_node[0], current_node[1], m, n)
                    _queue.extend(neighbors)
                        
        return nrof_islands
