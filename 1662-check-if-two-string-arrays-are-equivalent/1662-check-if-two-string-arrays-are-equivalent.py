class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        '''
        O(1) space solution
        class Solution:
            def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
                def getChars(word):
                    for s in word:
                        for c in s:
                            yield c
                    yield

                return all(c1 == c2 for c1, c2 in zip(getChars(word1), getChars(word2)))    
        '''
        '''
        call K = maxinum length of a char in word
        time: O(N*K)
        space: O(N*K)
        '''
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
        
