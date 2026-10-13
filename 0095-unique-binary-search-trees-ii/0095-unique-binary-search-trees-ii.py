# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:
        def build(start, end):
            if start > end:
                return [None]

            ans = []

            for i in range(start, end + 1):
                leftTrees = build(start, i - 1)
                rightTrees = build(i + 1, end)

                for left in leftTrees:
                    for right in rightTrees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        ans.append(root)

            return ans

        return build(1, n)
        