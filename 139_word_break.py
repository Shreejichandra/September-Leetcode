'''Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True
        #wordDict = set(wordDict)

        for i in range(len(s)):
            for j in range(i+1):
                if not dp[j]:
                    continue

                subword = s[j:i+1]
                if subword in wordDict:
                    dp[i+1] = True
                    break

        return dp[-1]
