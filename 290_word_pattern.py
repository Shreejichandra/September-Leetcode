'''Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.'''

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str_list = str.split(" ")
        d = defaultdict(int)
        values = []
        if len(str_list) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in d and str_list[i] not in values:
                d[pattern[i]] = str_list[i]
                values.append(str_list[i])
            
            elif pattern[i] not in d and str_list[i] in values:
                return False
            
            else:
                dict_word = d[pattern[i]]
                if dict_word == str_list[i]:
                    continue
                else:
                    return False
        return True
