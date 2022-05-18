# File: binarytree.py
# Date: April 27, 2021
# Author: COMP 120
# Description: Contains binary tree class,
#        with traversal methods.  

from collections import deque

class BinaryTreeNode:
    def __init__(self, val, left = None, right = None):
        """ 
        Initialize the node with a value,
        with left child from the parameter left 
        and the right child from the parameter right.
        """
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        """ 
        Returns string representation of the node,
        with just the value stored in the node.
        """
        return str(self.val)

class BinaryTree:
    def __init__(self, root = None):
        """ 
        Initialize the root of the tree
        from the parameter root.
        """
        self.root = root
    
    def is_bst(self):
        """
        Returns True if this binary tree (self) satisfies the
        search tree property.  The search tree property says
        that for every node in the tree, every val in its
        left subtree is less than it, and every val in its 
        right subtree is greater than it.
        Returns False otherwise.
        The empty tree satisfies the search tree property.
        Should use is_bst_recursive.
        """
        return self.is_bst_recursive(self.root, -999999999, 999999999)

    def is_bst_recursive(self, subtree_root, min_val, max_val):
        """
        Returns True if the binary subtree rooted at subtree_root
        satisfies the search tree property, and if the value of every 
        node of the subtree satisfies min_val < value < max_val.
        Returns False otherwise.
        The empty subtree satisfies the search tree property.
        """
        if subtree_root is None:
            return True
        if subtree_root.val <= min_val:
            return False
        if subtree_root.val >= max_val:
            return False
        return (self.is_bst_recursive(subtree_root.left, min_val, subtree_root.val) and 
                self.is_bst_recursive(subtree_root.right, subtree_root.val, max_val))

if __name__ == "__main__":
    # Test 1
    # Create tree nodes
    a = BinaryTreeNode(1)
    c = BinaryTreeNode(3)
    b = BinaryTreeNode(2, a, c)
    d = BinaryTreeNode(4, b, None)  
    l = BinaryTreeNode(11)
    k = BinaryTreeNode(10, None, l)
    p = BinaryTreeNode(15)
    o = BinaryTreeNode(14, None, p)
    m = BinaryTreeNode(12, k, o)
    i = BinaryTreeNode(8, d, m)

    # Create tree
    tree = BinaryTree(i)

    print("Test 1.  Should print True.")
    print(tree.is_bst())

    # Test 2
    # Create tree nodes
    a = BinaryTreeNode(1)
    c = BinaryTreeNode(3)
    b = BinaryTreeNode(2, a, c)
    d = BinaryTreeNode(9, b, None)  
    l = BinaryTreeNode(11)
    k = BinaryTreeNode(10, None, l)
    p = BinaryTreeNode(15)
    o = BinaryTreeNode(14, None, p)
    m = BinaryTreeNode(12, k, o)
    i = BinaryTreeNode(8, d, m)

    # Create tree
    tree = BinaryTree(i)

    print("Test 2.  Should print False.")
    print(tree.is_bst())

    # Test 3
    # Create tree nodes
    a = BinaryTreeNode(1)
    c = BinaryTreeNode(3)
    b = BinaryTreeNode(2, a, c)
    d = BinaryTreeNode(4, b, None)  
    p = BinaryTreeNode(15)
    o = BinaryTreeNode(14, None, p)
    m = BinaryTreeNode(7, k, o)
    i = BinaryTreeNode(8, d, m)

    # Create tree
    tree = BinaryTree(i)

    print("Test 3.  Should print False.")
    print(tree.is_bst())

    # Test 4
    # Create tree nodes
    a = BinaryTreeNode(2.5)
    c = BinaryTreeNode(3)
    b = BinaryTreeNode(2, a, c)
    d = BinaryTreeNode(4, b, None)  
    l = BinaryTreeNode(11)
    k = BinaryTreeNode(10, None, l)
    p = BinaryTreeNode(15)
    o = BinaryTreeNode(14, None, p)
    m = BinaryTreeNode(12, k, o)
    i = BinaryTreeNode(8, d, m)

    # Create tree
    tree = BinaryTree(i)

    print("Test 4.  Should print False.")
    print(tree.is_bst())   

    # Test 5
    # Create tree nodes
    a = BinaryTreeNode(1)
    c = BinaryTreeNode(3)
    b = BinaryTreeNode(2, a, c)
    d = BinaryTreeNode(4, b, None) 
    e = BinaryTreeNode(8.5)
    f = BinaryTreeNode(9.5)
    g = BinaryTreeNode(9, e, f)
    h = BinaryTreeNode(10, g, None)
    i = BinaryTreeNode(14)
    j = BinaryTreeNode(15)
    k = BinaryTreeNode(13, i, j)
    l = BinaryTreeNode(11, None, k)
    m = BinaryTreeNode(12, h, l)
    i = BinaryTreeNode(8, d, m)

    # Create tree
    tree = BinaryTree(i)

    print("Test 5.  Should print False.")
    print(tree.is_bst())

    # Test 6
    # Create tree nodes
    a = BinaryTreeNode(1)
    c = BinaryTreeNode(3)
    b = BinaryTreeNode(2, a, c)
    e = BinaryTreeNode(5)
    f = BinaryTreeNode(9.5)
    g = BinaryTreeNode(9, e, f)
    d = BinaryTreeNode(4, b, g)  
    l = BinaryTreeNode(11)
    k = BinaryTreeNode(10, None, l)
    p = BinaryTreeNode(15)
    o = BinaryTreeNode(14, None, p)
    m = BinaryTreeNode(12, k, o)
    i = BinaryTreeNode(8, d, m)

    # Create tree
    tree = BinaryTree(i)

    print("Test 6.  Should print False.")
    print(tree.is_bst())

    # Test 7
    # Create tree nodes
    a = BinaryTreeNode(1)
    c = BinaryTreeNode(3)
    b = BinaryTreeNode(2, a, c)
    d = BinaryTreeNode(4, b, None)  
    e = BinaryTreeNode(9)
    l = BinaryTreeNode(11, e, None)
    k = BinaryTreeNode(10, None, l)
    p = BinaryTreeNode(15)
    o = BinaryTreeNode(14, None, p)
    m = BinaryTreeNode(12, k, o)
    i = BinaryTreeNode(8, d, m)

    # Create tree
    tree = BinaryTree(i)

    print("Test 7.  Should print False.")
    print(tree.is_bst())
