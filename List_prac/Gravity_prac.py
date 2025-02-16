N = int(input())
box = list(map(int, input().split()))
max_fall = 0
for i in range(N-1):    # 마지막 상자는 확인할 필요x
    cnt = 0         # 자신보다 작은 상자 개수
    for j in range(i+1, N):
        if box[i] > box[j]:
            cnt += 1
    if max_fall < cnt:
        max_fall = cnt
print(max_fall)