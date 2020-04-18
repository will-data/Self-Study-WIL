import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        queue = [root]
        while queue:
            root = queue.pop()
            if root:
                print(root.data, end =' ')
                queue.insert(0,root.left)
                queue.insert(0,root.right)

T=int(input())