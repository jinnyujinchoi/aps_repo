# baby-gin 문제 (완탐 버전)
#   - 숫자 3개 연속되었는가(run)
#   - 숫자 3개가 같은가(triplet)
# 6자리 숫자 입력
# -> 모든 순서를 보아야 한다 (순열)

'''
6 6 7 7 6 7
0 5 4 0 6 0
1 0 1 1 2 3
'''

path = []
used = [0]*6
bgn_result = False

def is_baby_gin():
    cnt = 0
    # run + triplet 개수 합 = 2
    # 앞에서 3개
    a, b, c = path[0], path[1], path[2]
    if a == b == c:
        cnt += 1
    elif a == (b-1) == (c-2):
        cnt += 1
    # 뒤에서 3개
    a, b, c = path[3], path[4], path[5]
    if a == b == c:
        cnt += 1
    elif a == (b - 1) == (c - 2):
        cnt += 1

    return cnt == 2

def recur(cnt):
    global bgn_result
    if cnt == 6:
        # baby-gin 인지 검사
        if is_baby_gin():
            bgn_result = True
        return

    for idx in range(6):
        # idx를 이미 썼다면, 뽑지마라
        if used[idx]:
            continue

        used[idx] = 1
        path.append(arr[idx])
        recur(cnt+1)
        path.pop()
        used[idx] = 0

arr = list(map(int, input().split()))
recur(0)

print('YES') if bgn_result else print('NO')

