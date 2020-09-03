'''Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.''' 

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, (n//2)+1):
            s1 = ""
            new = ""
            if n % i == 0:
                s1 += s[:i]
                times = n // i
                new = s1 * times
                #print(new)
                if new == s:
                    return True
        return False
            
       
            
            
        
