N=int(input())
box=list(map(int,input().split()))
max_v=0
for i in range(N-1):
    fall_cnt = 0
    for j in range(i+1,N):
        if box[i] > box[j]:
            fall_cnt += 1
    if max_v < fall_cnt:
        max_v = fall_cnt
print(max_v)