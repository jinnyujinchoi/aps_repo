'''
9
7 4 2 0 0 6 0 7 0
=> 7
9
4 2 0 0 7 6 0 7 0
=> 5
'''
N = int(input())
box = list(map(int, input().split()))
max_v = 0 # 낙차 값 초기화
for i in range(N-1): # 마지막 값x -> 순회할 필요x
    cnt = 0         # 오른쪽에 자신보다 더 낮은 박스 개수(낙차)
    for j in range(i+1, N): # j는 자신 제외 오른쪽 박스
        if box[i] > box[j]: # 자신보다 값이 작으면
            cnt += 1    # 더 낮은 박스면 낙차 추가
    if max_v < cnt:
        max_v = cnt
print(max_v)