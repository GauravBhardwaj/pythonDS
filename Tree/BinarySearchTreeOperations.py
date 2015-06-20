__author__ = 'gbhardwaj'
from TreeNode import TreeNode


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def inorder_traversal(self, root_node):
        if not root_node:
            return None
        else:
            current = root_node
            self.inorder_traversal(current.left_child)
            print current.data
            self.inorder_traversal(current.right_child)


    def search(self, search_data):
        if not self.root:
            return None
        else:
            current = self.root
            while True:
                if current.data == search_data:
                    return "match found"
                    break
                elif current.data > search_data:
                    current = current.left_child
                elif current.data < search_data:
                    current = current.right_child
                else:
                    return "match not found"
                    break



    def insert(self, new_data):

        if not self.root:
            self.root = TreeNode(new_data)
            self.size += 1
        else:
            current = self.root
            while True:
                if current.data > new_data:
                    # go left
                    if current.left_child:
                        current = current.left_child
                    else:
                        current.left_child = TreeNode(new_data)
                        self.size += 1
                        break
                elif current.data < new_data:
                    #go right
                    if current.right_child:
                        current = current.right_child
                    else:
                        current.right_child = TreeNode(new_data)
                        self.size += 1
                        break
                else:
                    break

    def size_recusrive(self, root_node):
        if not root_node:
            return 0
        else:
            return 1+(self.size_recusrive(root_node.left_child) + self.size_recusrive(root_node.right_child))

    def size_iterative(self, root_node):
        size = 0
        if not root_node:
            return size
        else:
            traversal_list = [root_node]
            while len(traversal_list) > 0:

                current = traversal_list.pop(0)
                if current:
                    size += 1
                    traversal_list.append(current.left_child)
                    traversal_list.append(current.right_child)
        return size
    def height(self, node):
        '''
        it is the number of steps needed to get from the node
        to the deepest leaf in either of the node's subtrees
        :param node: for which we are calculating the height
        :return: height
        '''
        if not node:
            return -1
        else:
            return 1 + max(self.height(node.left_child), self.height (node.right_child))


    def BFS(self, root_node):
        '''
        traversal for breadth first search
        :param root_node:
        :return:
        '''
        if not root_node:
            return None
        list_traversal = [root_node]
        # deque.append(root_node)
        while len(list_traversal) > 0:
            # print "Breadth first traversal"
            current = list_traversal.pop(0)
            print current.data
            if current.left_child:
                list_traversal.append(current.left_child)
            if current.right_child:
                list_traversal.append(current.right_child)

    def DFS(self, root_node):
        '''
        Depth first search
        :param root_node:
        :return:
        '''
        if not root_node:
            return None
        list_traversal = [root_node]
        while len(list_traversal):
            current = list_traversal.pop()
            print current.data
            if current.right_child:
                list_traversal.append(current.right_child)
            if current.left_child:
                list_traversal.append(current.left_child)


    def mirror_tree(self, root_node):
        if not root_node:
            return None

        # current = root_node
        self.mirror_tree(root_node.left_child)
        self.mirror_tree(root_node.right_child)
        # self.swap(root_node, root_node.left_child, root_node.right_child)
        # swap element references
        root_node.left_child = root_node.right_child
        root_node.right_child = root_node.left_child

        return root_node

    def lowest_common_ancestor(self, root_node, nodea, nodeb):
        if not root_node:
            return None
        if root_node.data > nodea.data and root_node.data > nodeb.data:
            return self.lowest_common_ancestor(root_node.right_child, nodea, nodeb)
        if root_node.data < nodea.data and root_node.data < nodeb.data:
            return self.lowest_common_ancestor(root_node.left_child, nodea, nodeb)


    def lowest_common_ancestor_iterative(self, root_node, nodea, nodeb):
        '''
        This is iterative solution and O(n) time and O(1) space
        :param root_node:
        :param nodea:
        :param nodeb:
        :return:
        '''
        if not root_node:
            print "root node doesnt exists"
            return None

        current = root_node
        while current:
            if current.data > nodea.data and current.data > nodeb.data:
                print "it goes to left side"
                current = current.left_child

            elif current.data < nodea.data and current.data < nodeb.data:
                print "goes to right side"
                current = current.right_child

            else:
                return root_node.data









