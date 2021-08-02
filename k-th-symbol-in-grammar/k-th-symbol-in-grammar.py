class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return "0"

        parent_number = self.kthGrammar(n-1, (k+1)//2)
        current_number = "01" if parent_number == "0" else "10"
    #         k % 2 is either 0 or 1
        return current_number[(k+1) % 2]
    
