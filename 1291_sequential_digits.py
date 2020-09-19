'''An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.'''

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        min_len = len(str(low))
        max_len = len(str(high))
        ans = []
       
        curr_len = min_len
        i = 0
        
        while i < len(digits)-curr_len+1:
            while curr_len <= max_len and i <= len(digits)-curr_len:
                possible_digits = digits[i: i + curr_len]
                possible_num = int("".join(str(k) for k in possible_digits))
                if low <= possible_num <= high:
                    ans.append(possible_num)
                curr_len += 1
            curr_len = min_len
            i += 1
            
        return sorted(ans)
