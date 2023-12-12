import copy


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        '''
        time: len(words) * max(len(word[i])) ~ O(N*K)
        space: len(chars)*len(words) ~ O(N*L)
        '''
        # turn chars into hash map for faster query time, key=char, value=nrof chars
        chars_map = {}
        for char in chars:
            if char not in chars_map:
                chars_map[char] = 1
            else:
                chars_map[char] += 1

        good_strings_len = 0

        for word in words:
            # chars_map reset for each word
            break_flag = False
            word_chars_map = copy.deepcopy(chars_map)
            for idx, char in enumerate(word):
                if char in word_chars_map:
                    # get one char
                    word_chars_map[char] -= 1
                    # if there is no char left, remove it
                    if word_chars_map[char] == 0:
                        word_chars_map.pop(char)
                else:
                    break_flag = True
                    break
            # idx reach word end mean that all char in word is formed
            # idx start at 0, so needed to add one for lenght
            # in case that len(word)==1, even when break, good_strings_len still got += 1p,
            # fix this by detect break event with break_flag
            if not break_flag:
                good_strings_len += len(word)

            
        return good_strings_len