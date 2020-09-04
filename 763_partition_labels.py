'''
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that 
each letter appears in at most one part, and return a list of integers representing the size of these parts.
'''

from collections import defaultdict
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        set_s = set(S)
        n = len(S)
        ans = []
        d = defaultdict(int)
        for letter in set_s:
            x = S[::-1].find(letter)
            x = n - x - 1
            d[letter] = x
        i = 0
        index = -1
        while index != n-1:
            i = index+1
            index = d[S[i]]
            substring = S[i:index+1]
            k = i
            while i < index:
                if d[S[i]] > index:
                    index = d[S[i]]  
                    substring = S[k: index+1]
                i += 1
         
            ans.append(len(substring))
        #print(substring)
        return ans
