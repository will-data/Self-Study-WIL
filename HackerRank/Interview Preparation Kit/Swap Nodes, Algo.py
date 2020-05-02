#!/bin/python3

import os
import sys
import sys

sys.setrecursionlimit(2000)


# Define class Node
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = 1

    def __str__(self):
        return str(self.info)


# I referred to snoopybox's blog; https://www.snoopybox.co.kr/1825
## And wrote code below by myself.
class Tree:
    def __init__(self):
        self.root = Node(1)

    def createTree(self, data):
        nodeQueue = [self.root]
        data.reverse()
        while nodeQueue:
            current = nodeQueue.pop()
            left, right = data.pop()
            if left != -1:
                current.left = Node(left)
                current.left.level = current.level + 1
                nodeQueue.insert(0, current.left)
            if right != -1:
                current.right = Node(right)
                current.right.level = current.level + 1
                nodeQueue.insert(0, current.right)

    def swapNode(self, query):
        nodeQueue = [self.root]
        while nodeQueue:
            current = nodeQueue.pop()
            if current.level % query == 0:
                current.left, current.right = current.right, current.left
            if current.left:
                nodeQueue.insert(0, current.left)
            if current.right:
                nodeQueue.insert(0, current.right)


def inOrder(node, printResult):
    if node:
        inOrder(node.left, printResult)
        printResult.append(node.info)
        inOrder(node.right, printResult)
    return printResult


def swapNodes(indexes, queries):
    givenTree = Tree()
    givenTree.createTree(indexes)
    results = []
    for query in queries:
        givenTree.swapNode(query)
        result = inOrder(givenTree.root, [])
        results.append(result)
    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    indexes = []
    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))
    queries_count = int(input())
    queries = []
    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
