class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        
        if len(s) % 2 == 1:
            return False
        
        def is_parenthesis(candidate):
            return candidate in ["()", "[]", "{}"]
        
        stack = deque()
        
        for bracket in s:
            # if is opening bracket
            if bracket in ["(", "[", "{"]:
                stack.append(bracket)
            # if is closing bracket 
            else:
                if not stack:
                    return False
                
                top_bracket = stack.pop()
                if not is_parenthesis(top_bracket+bracket):
                    return False
                
        if stack:
            return False

                        
        return True
            
                