# Given the root node of a binary search tree, return the sum of values of all 
# nodes with value between L and R(inclusive).
# The binary search tree is guaranteed to have unique values.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def rangeSumBST(root, L, R): return 0 if root == None else int(L <= root.val <= R) * root.val + rangeSumBST(root.left, L, R) + rangeSumBST(root.right, L, R)
