import sys
import math
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes=[]
        self.storeBSTNodes(self, root, nodes)
        n=len(nodes)
        return self.buildTreeUtil(self,nodes,0,n-1)
      
    def storeBSTNodes(self, root,nodes):
      if not root:
        return
      self.storeBSTNodes(self,root.left,nodes)
      nodes.append(root)
      self.storeBSTNodes(self,root.right,nodes)
      
    def buildTreeUtil(self,nodes,start,end):
      if start>end:
        return None
    
    
      mid=(start+end)//2
      node=nodes[mid]
      # Using index in Inorder traversal, construct
      # left and right subtress
      node.left=self.buildTreeUtil(self,nodes,start,mid-1)
      node.right=self.buildTreeUtil(self,nodes,mid+1,end)
      return node

def preOrder(root):
    if not root:
        return
    print("{} ".format(root.data),end="")
    preOrder(root.left)
    preOrder(root.right)

if __name__=='__main__':
    root = TreeNode(10)
    root.left = TreeNode(8)
    root.left.left = TreeNode(7)
    root.left.left.left = TreeNode(6)
    root.left.left.left.left = TreeNode(5)
    root = Solution.balanceBST(Solution,root)
    print("Preorder traversal of balanced BST is :")
    preOrder(root)