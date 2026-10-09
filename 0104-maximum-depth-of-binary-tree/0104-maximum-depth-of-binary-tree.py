# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        q = deque()
        if not root:
            return 0
        q.append(root)
        maxdepth = 0
        while q:
            maxdepth += 1
            level_len = len(q)
            
            for _ in range(level_len):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return maxdepth
        