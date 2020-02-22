# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        global nums
        nums = []
        def inorder(root,nums):
            if not root:
                return
            inorder(root.left,nums)
            nums.append(root.val)
            inorder(root.right,nums)
        inorder(root,nums)
        min_diff = sys.maxsize
        for i in range(len(nums)-1):
            min_diff = min(abs(nums[i] - nums[i+1]),min_diff)
        return min_diff