class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        
        def recur_fib(num):
            if num == 0:
                return 0
            if num == 1:
                return 1
            
            if num not in cache:
                val = recur_fib(num-1) + recur_fib(num-2)
                cache[num] = val
            else:
                val = cache[num]
            
            return val
        
        return recur_fib(n)