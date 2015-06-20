__author__ = 'gbhardwaj'

from TreeNode import TreeNode
from BinarySearchTreeOperations import BinarySearchTree
'''
       10
  5         15

1   6    11    50

'''
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(1)
bst.insert(6)
bst.insert(11)
bst.insert(50)

print bst.root.data
print "size of tree after insertions is: " + str(bst.size)

print "size of tree using recursion"
print bst.size_recusrive(bst.root)

print "size of tree using iterative method"
print bst.size_iterative(bst.root)

print "height of tree"
print bst.height(bst.root)

print "inorder traversal: "
bst.inorder_traversal(bst.root)

print "breadth first traversal: "
bst.BFS(bst.root)

print "depth first traversal: "
bst.DFS(bst.root)

print "lowest common ancestor between two nodes"
print bst.lowest_common_ancestor(bst.root, bst.root.right_child, bst.root.left_child)

print "mirror image of a tree"
root_node = bst.mirror_tree(bst.root)

print "depth first traversal after mirroring: "
bst.DFS(bst.root)

print "breadth first traversal after mirroring: "
bst.BFS(bst.root)

