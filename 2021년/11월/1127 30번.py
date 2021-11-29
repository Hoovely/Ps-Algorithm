# 백준_13116_30번_트리_실버 4

tree = [0 for _ in range(1024)]

for i in range(1, 512): # 트리 생성
    tree[2*i] = i
    tree[2*i+1] = i

for _ in range(int(input())):
    a,b = map(int,input().split())
    tree_a, tree_b = [], []
    while a > 0: # tree_a에 a부터 1까지의 노드를 저장한다
        tree_a.append(a)
        a = tree[a]
    while b > 0: # tree_b에 b부터 1까지의 노드를 저장한다
        tree_b.append(b)
        b = tree[b]
    
    flag = False
    for i in tree_a:
        for j in tree_b:
            if i == j:
                flag = True
                break
        if flag:
            print(i*10)
            break