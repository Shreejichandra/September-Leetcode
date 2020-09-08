# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, num):
        num += str(root.val)
        if root.left:
            self.dfs(root.left, num)
        if root.right:
            self.dfs(root.right, num)
        if not root.left and not root.right:
            self.ans += int(num, 2)
            
        return self.ans
                
    def sumRootToLeaf(self, root: TreeNode) -> int: 
        num = ""
        self.ans = 0
        final = self.dfs(root, num)
     
        return final
