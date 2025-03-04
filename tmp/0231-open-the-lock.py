class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        # by appling Queue and BFS, the number of iteration steps when we meet target is the shortest number of steps
        # when meet with deadends, we abbandon that iterations

        from collections import deque

        queue = deque()
        visited = set()
        lock = '0000'
        turns = 0

        def _get_lock_num(num):
            if num == -1:
                return 9
            return num % 9

        def _get_neighbor_locks(lock):
            # check and return from 4*2 next lock state
            return [
                lock[:3] + str(_get_lock_num(int(lock[3])+1)),
                lock[:3] + str(_get_lock_num(int(lock[3])-1)),
                lock[:2] + str(_get_lock_num(int(lock[2])+1)) + lock[3],
                lock[:2] + str(_get_lock_num(int(lock[2])-1)) + lock[3],
                lock[0] + str(_get_lock_num(int(lock[1])+1)) + lock[2:],
                lock[0] + str(_get_lock_num(int(lock[1])-1)) + lock[2:],
                str(_get_lock_num(int(lock[0])+1)) + lock[1:],
                str(_get_lock_num(int(lock[0])-1)) + lock[1:],
            ]

        # add root node
        queue.append(lock)
        while len(queue):
            lock = queue.popleft()
            print(lock)
            visited.add(lock)
            neighbors = _get_neighbor_locks(lock)
            for next_lock in neighbors:
                if next_lock not in deadends and next_lock not in visited:
                    queue.append(next_lock)
            turns += 1

        return turns
