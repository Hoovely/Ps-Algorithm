# 백준_1991_트리 순회_트리_실버 1
# 오답 1

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])


def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])


def postorder(root):
    if root != '.':
        postorder(tree[root][0])
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
