# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        ans = 0
        queue = collections.deque([root])

        while (queue):
            queueLen = len(queue)

            for i in range(queueLen):
                node = queue.popleft()
                if node:
                    values.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
        
        sortedVal = values.sort()

        for i in range(k):
            ans = values[i] 

        return ans                   