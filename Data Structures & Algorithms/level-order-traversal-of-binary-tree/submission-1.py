# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root,0)])
        res = [[root.val]]
        
        while queue:
            curr = queue.popleft()
            level = curr[1]
            if curr[0].left:
                queue.append((curr[0].left, level+1))
                if len(res) <= level+1:
                    res.append([])
                res[level+1].append(curr[0].left.val)
            if curr[0].right:
                queue.append((curr[0].right, level+1))
                if len(res) <= level+1:
                    res.append([])
                res[level+1].append(curr[0].right.val)
        
        return res
            


        