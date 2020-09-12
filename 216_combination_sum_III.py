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
