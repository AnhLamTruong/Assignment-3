2.  Construct Binary Tree from Preorder and Inorder Traversal

- The first element in the array is always the root of the tree, the sublist of the array will be recursively constructed. The inoder array helps me to know that, which elements will be in the left and right. Therefore, my method will use recursive the sublist of the array from the left to the mid and mid to the right.

3.  Binary Tree Maximum Path Sum

- I use the DFS to solve the problem. I firstly calculate the subtree with the split and add it into the res[0], but I return the maximum between the path and the res[0]. Therefore, if the path is not bigger than the path which is splited, the function simply returns the res[0]

4. Find Largest Value in Each Tree Row

- Use BFS to traversal the tree level by level. Find the max value of each level and append to the res list. To traversal each level we need to know the size of each level and this is the key point. We traversal all elements of the tree once so total time complexity is O(n)

5. Balance a Binary Search Tree

- Traverse given BST in inorder and store result in an array. This step takes O(n) time. Note that this array would be sorted as inorder traversal of BST always produces sorted sequence.
