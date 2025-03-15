class MinStack(object):

    def __init__(self):
        self._stack = []
        self._min_stack = []
        self._len = 0

    def _insert_min_stack(self, val):
        for idx in range(self._len):
            if val <= self._min_stack[idx]:
                self._min_stack = self._min_stack[:idx] + [val] + self._min_stack[idx:]
                return
        else:
            self._min_stack.append(val)

    def _remove_min_stack(self, val):
        for idx in range(self._len):
            if val == self._min_stack[idx]:
                self._min_stack = self._min_stack[:idx] + self._min_stack[idx+1:]
                return


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self._stack.append(val)
        self._insert_min_stack(val)
        self._len += 1


    def pop(self):
        """
        :rtype: None
        """
        val = self._stack.pop(-1)
        self._remove_min_stack(val)
        self._len -= 1

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self._min_stack[0]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
