#Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        all_combo = list(combinations(numbers[:n], k))
        print(all_combo)
        ans = []
        for combo in all_combo:
            if sum(combo) == n:
                ans.append(combo)
        #print(ans)
        return ans
