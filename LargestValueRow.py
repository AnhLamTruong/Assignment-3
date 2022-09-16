# Definition for a binary tree node.
import collections
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode],d: int) -> List[int]:
        if not root: return []
        res = []
        queue = collections.deque([root])
        while queue:
            largest = -float('inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.val > largest:
                    largest = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(largest)
        return res
        
        
# Driver Code
if __name__ == "__main__":
  root = TreeNode(4)
  root.left = TreeNode(9)
  root.right = TreeNode(2) 
  root.left.left = TreeNode(3)
  root.left.right = TreeNode(5)
  root.right.right = TreeNode(7)
  print(Solution.largestValues(Solution,root,0))          