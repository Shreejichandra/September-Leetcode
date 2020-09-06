'''Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?'''

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        a_index = []
        b_index = []
        d = defaultdict(int)
        for row in range(len(A)):
            for column in range(len(A[0])):
                if A[row][column] == 1:
                    a_index.append((row, column)) 
                    
                if B[row][column] == 1:
                    b_index.append((row, column))
        
        for a_r, a_c in a_index:
            for b_r, b_c in b_index:
                d[(b_r - a_r, b_c-a_c)] += 1
         
        return max(d.values() or [0])
            
            
