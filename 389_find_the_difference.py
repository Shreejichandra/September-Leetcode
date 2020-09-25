'''Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for ch in s:
            t = t.replace(ch, "", 1)
        return t