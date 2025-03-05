'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def pre_order(n):       # 전위순회 방문한 정점 먼저 처리
    global cnt
    if n:
        print(n, end=' ')        # visit(n) n에서 할 일 처리
        cnt += 1
        pre_order(l[n])
        pre_order(r[n])

def in_order(n):        # 중위순회
    if n:
        in_order(l[n])
        print(n, end=' ')        # visit(n) n에서 할 일 처리
        in_order(r[n])

def post_order(n):
    if n:
        post_order(l[n])
        post_order(r[n])
        print(n, end=' ')

N = int(input())        # 1~N까지의 정점
E = N-1                 # 간선 수
arr = list(map(int, input().split()))

l = [0]*(N+1)
r = [0]*(N+1)
par = [0]*(N+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    par[c] = p
    if l[p] == 0:
        l[p] = c
    else:
        r[p] = c

root = 1
for i in range(1, N+1):
    if par[i] == 0:
        root = i
        break

cnt = 0
post_order(root)
# print(cnt)