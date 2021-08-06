# 백준_1991_트리 순회_트리_실버 1

import sys
input = sys.stdin.readline


def preorder(root):
    print(root, end='')
    if tree[root][0] != '.':
        preorder(tree[root][0])
    if tree[root][1] != '.':
        preorder(tree[root][1])


def inorder(root):
    if tree[root][0] != '.':
        inorder(tree[root][0])
    print(root, end='')
    if tree[root][1] != '.':
        inorder(tree[root][1])


def postorder(root):
    if tree[root][0] != '.':
        postorder(tree[root][0])
    if tree[root][1] != '.':
        postorder(tree[root][1])
    print(root, end='')


n = int(input())
tree = {}
for _ in range(n):
    p, l, r = input().strip().split()
    tree[p] = [l, r]

preorder('A')
print()
inorder('A')
print()
postorder('A')
