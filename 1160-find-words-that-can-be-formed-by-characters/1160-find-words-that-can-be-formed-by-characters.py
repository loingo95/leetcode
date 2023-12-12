class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # turn chars into hash map for faster query time, key=char, value=nrof chars
        chars_counts = defaultdict(int)
        for char in chars:
            chars_counts[char] += 1

        good_strings_len = 0

        # 1st try
        # time: len(words) * max(len(word[i])) ~ O(N*K)
        # space: len(chars)*len(words) ~ O(N*L)
        
        # import copy
        # for word in words:
        #     # chars_map reset for each word
        #     break_flag = False
        #     word_chars_map = copy.deepcopy(chars_map)
        #     for idx, char in enumerate(word):
        #         if char in word_chars_map:
        #             # get one char
        #             word_chars_map[char] -= 1
        #             # if there is no char left, remove it
        #             if word_chars_map[char] == 0:
        #                 word_chars_map.pop(char)
        #         else:
        #             break_flag = True
        #             break
        #     # idx reach word end mean that all char in word is formed
        #     # idx start at 0, so needed to add one for lenght
        #     # in case that len(word)==1, even when break, good_strings_len still got += 1p,
        #     # fix this by detect break event with break_flag
        #     if not break_flag:
        #         good_strings_len += len(word)

            
        # 2nd try with requency of letters hint
        for word in words:
            # build word chars map
            word_chars_counts = defaultdict(int)
            for char in word:
                word_chars_counts[char] += 1
            
            # now do comparison
            good = True
            for char in word_chars_counts:
                # if chars_map do not have char, then return 0
                if word_chars_counts[char] > chars_counts.get(char, 0):
                    good = False
                    break
            if good:
                good_strings_len += len(word) 
            
        return good_strings_len