class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        combinations = [""]
        for digit in digits:
            new_combinations = []
            for char in digit_to_char[digit]:
                new_combinations += [comb+char for comb in combinations]
            combinations = new_combinations
            
        return combinations