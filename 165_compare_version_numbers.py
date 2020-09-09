'''Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number.
Its third and fourth level revision number are both 0.'''

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        num1 = version1.split('.')
        num2 = version2.split('.')
        n1 = len(num1)
        n2 = len(num2)

        if n1 > n2:
            num2 += [0] * (n1 - n2)
           
        else:
            num1 += [0] * (n2 - n1)
        #print(num1, num2)
            
        for i in range(len(num1)):
            if int(num1[i]) < int(num2[i]):
                return -1
            if int(num1[i]) > int(num2[i]):
                return 1
        return 0
            
