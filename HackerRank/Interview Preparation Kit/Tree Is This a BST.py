""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def checkBST(root):
    def inOrder(root, inOrderL):
        if root.left:
            inOrder(root.left, inOrderL)
        if root.data:
            inOrderL.append(root.data)
        if root.right:
            inOrder(root.right, inOrderL)
        return inOrderL

    leafArray = inOrder(root, [])

    if (len(set(leafArray)) == len(leafArray)) and leafArray == sorted(leafArray):
        return True
    else:
        return False


