# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root:
            return self.helper(root, None, None)

    def helper(self, root, mini, maxi):
        if root:
            left_valid = (root.left is None or 
                (root.left.val < root.val and 
                (mini is None or root.left.val > mini)))
            right_valid = (root.right is None or 
                (root.right.val > root.val and 
                (maxi is None or root.right.val < maxi)))
            if left_valid and right_valid:
                return self.helper(root.left, mini, root.val) and self.helper(root.right, root.val, maxi)
            return False
        return True