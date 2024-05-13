'''
Created by sunwoong on 2024/05/13

풀이 시간 - 40분
'''
import sys
sys.setrecursionlimit(10 ** 6)

class Node:
    def __init__(self):
        self.idx = None
        self.value = None
        self.left = None
        self.right = None
    
def insert(node, info):
    if not node:
        new_node = Node()
        new_node.idx = info[0]
        new_node.value = info[1]
        return new_node
    if node.value > info[1]:
        node.left = insert(node.left, info)
    else:
        node.right = insert(node.right, info)
    return node

def preorder(node, order):
    if not node:
        return
    order.append(node.idx)
    preorder(node.left, order)
    preorder(node.right, order)

def postorder(node, order):
    if not node:
        return
    postorder(node.left, order)
    postorder(node.right, order)
    order.append(node.idx)

def solution(nodeinfo):
    orders = [i for i in range(1, len(nodeinfo) + 1)]
    nodeinfo = sorted(list(zip(orders, nodeinfo)), key=lambda x: (-x[1][1], x[1][0]))
    root = None
    for i, node in nodeinfo:
        root = insert(root, (i, node[0]))
    preorders = []
    postorders = []
    preorder(root, preorders)
    postorder(root, postorders)
    return [preorders, postorders]