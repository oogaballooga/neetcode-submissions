# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        val, found = self.inOrder(root, k, 1)
        return val
    

    def inOrder(self, root, k, curr):
        if root is None:
            return (curr-1, False)

        leftCurr, leftFound = self.inOrder(root.left, k, curr)
        if leftFound:
            return (leftCurr, True)

        curr = leftCurr+1
        if curr == k:
            return (root.val, True)

        rightCurr, rightFound = self.inOrder(root.right, k, curr+1)
        if rightFound:
            return (rightCurr, True)
        return (rightCurr, False)
        