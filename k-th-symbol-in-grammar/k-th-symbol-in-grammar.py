class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return self.recursive("", n-1, k-1)
    
    def recursive(self, parent_number, n, k):
        if n == 0:
            return "0"
        
        parent_number = self.recursive(parent_number, n-1, k//2)
        current_number = "01" if parent_number == "0" else "10"
#         k % 2 is either 0 or 1
        return current_number[k % 2]