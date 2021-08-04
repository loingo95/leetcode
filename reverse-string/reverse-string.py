class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.doRecursion(s, 0, len(s) - 1)
        
    
    def doRecursion(self, string, left, right):
        if left >= right:
            return
        
        string[left], string[right] = string[right], string[left]
        
        self.doRecursion(string, left+1, right-1)
        