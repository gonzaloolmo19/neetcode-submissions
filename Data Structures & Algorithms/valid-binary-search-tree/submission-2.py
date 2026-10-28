# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, upper, lower):
            if not root:
                return True
            
            if root.val <= lower or root.val >= upper:
                return False
            
            left = True if not root.left else dfs(root.left, root.val, lower)
            right = True if not root.right else dfs(root.right, upper, root.val)

            return left and right
        
        return dfs(root, float("inf"),-float("inf"))