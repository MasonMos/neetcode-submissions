# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        bst = []

        deque = collections.deque([root])

        while (deque):
            dequeLen = len(deque)
            levels = []
            for i in range(dequeLen):
                node = deque.popleft()
                if node is not None:
                    levels.append(node.val)
                    deque.append(node.left)
                    deque.append(node.right)
            if levels:
                bst.append(levels)

        return bst
