class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1_str = "".join(word1)
        word2_str = "".join(word2)

        # early check base on string lenght
        if len(word1_str) != len(word2_str):
            return False

        # if reach here, two word_str have the same length
        word_lenght = len(word1_str)
        for idx in range(word_lenght):
            if word1_str[idx] != word2_str[idx]:
                return False
        return True
        
