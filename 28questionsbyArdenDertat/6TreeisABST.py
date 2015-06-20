#Given a binary tree, check whether it’s a binary search tree or not.


def isBST(self,root):
    '''
    recursion, compare every right and left child but this method would be errors in case BST have grandparent
    lesser than parent
    '''

    if not root:
        return True
    if root.left and root.left.data > root.data:
        return False
    if root.right and root.right.data < root.data:
        return False
    if not isBST(root.left) or not isBST(root.right):
        return False
    return True


def isBST1(self, root, minval, maxval):
    '''
    Keep the minimum and maximum range for all elements of the tree,
    root can have any value from -infinity to +infinity
    however all right childs of root can have only values root.data to +infinity, similarily
    all left childs of root can have values in range -infinity
    Root value will be in range from -infinity to +infinity
    '''
    #minval = float("infinity")
    #maxval = floar("-infinity")
    if not root:
        return
    if not minval <= root.data <= maxval:
        return False
    if isBST(root.left, minval, root.data) and isBST(root.right, root.data, maxval):
        return True


def isBST2(self, root):
    '''
    If we traverse the tree inorder wise, we should get a sorted sequence, so we
    can check wether next element is greater than previous
    inorder: right , root, left
    '''
    alist = [self.root.data]
    temp = self.root

    while len(alist) > 0:
        curr = alist.pop(1)
        print cur.data
        if curr.left:
            alist.append(curr.left)
        if curr.right:
            alist.append(curr.right)


def traverse(self, root):
    '''
    '''
    if not root:
        return
    else:
        print root.data
        traverse(root.left)
        traverse(root.right)
