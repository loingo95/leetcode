class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def recur_pow(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            if n < 0:
                return 1/recur_pow(x, -n)

            if n%2 == 0:
                return recur_pow(x*x, n//2)
            
            else:
                return recur_pow(x*x, n//2)*x
        
        return recur_pow(x, n)

