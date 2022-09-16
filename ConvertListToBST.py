#Link List Node
from itertools import count
import re


class ListNode:
  def __init__(self):
    self.data=None
    self.next=None
#BST Node
class TreeNode:
  def __init__(self):
    self.data=None
    self.left=None
    self.right=None



class Solution(object):
  # This function counts the number of 
  # nodes in Linked List and then calls 
  # sortedListToBSTRecur() to construct BST 
    def sortedListToBST(self, head):
      n=countLNodes(head)
      return self.sortedListToBSTRecur(Solution,n,head);
    # The main function that constructs 
    # balanced BST and returns root of it. 
    # head -. Pointer to pointer to 
    # head node of linked list n -. No.
    # of nodes in Linked List 
    def sortedListToBSTRecur(self,n,head):
      #Base Case
      if(n<=0):
        return None
      left=self.sortedListToBSTRecur(Solution,int(n/2),head)
      
      #Allocate memory for root, and link the above
      #constructed left subtree with the root
      root=newNode(head.data)
      root.left=left
      # Change head pointer of Linked List
      # for parent recursive calls
      head = (head).next
      
      # Recursively construct the right 
      # subtree and link it with root 
      # The number of nodes in right subtree
      # is total nodes - nodes in 
      # left subtree - 1 (for root) which is n-n/2-1
      root.right=self.sortedListToBSTRecur(Solution,n-int(n/2)-1,head)
      return root;      
      



#Helper function
#Function that count the Nodes in the given Linked List
def countLNodes(head):
  count=0
  temp=head
  while(temp!=None):
    temp=temp.next
    count+=1;
  return count;

#Function that push an element into the Linked List
def push(head,new_data):
  new_node=ListNode()
  new_node.data=new_data
  new_node.next=head
  head=new_node
  return head

#Function to print nodes in the given Linked List
def printList(node):
  while(node!=None):
    print(node.data, end=' ')
    node=node.next

#BST function helper
def newNode(data):
  node=TreeNode()
  node.data=data
  node.left=None
  node.right=None
  return node

#Print preorder traversal of BST using Recusion
def preOrder(node):
  if (node==None):
    return
  print(node.data, end=' ')
  preOrder(node.left)
  preOrder(node.right)
  
  
#Driver code
head=None

# Let us create a sorted linked list to test the functions 
# Created linked list will be 1.2.3.4.5.6.7 
head = push(head, 7) 
head = push(head, 6) 
head = push(head, 5) 
head = push(head, 4) 
head = push(head, 3) 
head = push(head, 2) 
head = push(head, 1) 

print("Given Linked List")
printList(head)
#Conver List to BST
root=Solution.sortedListToBST(Solution,head)
print("\n Constructed BST:")
preOrder(root)