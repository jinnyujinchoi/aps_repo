used = [0]*6
path = []
bgn_result = False
# baby-gin 확인 함수
def is_babygin():
    cnt = 0
    a, b, c = path[0], path[1], path[2]
    if a == b == c:
        cnt += 1
    elif a == (b-1) == (c-2):
        cnt += 1

    a, b, c = path[3], path[4], path[5]
    if a == b == c:
        cnt += 1
    elif a == (b-1) == (c-2):
        cnt += 1

    return cnt == 2

# 재귀
def recur(cnt):
    global bgn_result
    if cnt == 6:
        # baby-gin 확인
        if is_babygin():
            bgn_result = True
        return

    for idx in range(6):
        if used[idx]:
            continue
        used[idx] = 1
        path.append(arr[idx])
        recur(cnt + 1)
        path.pop()
        used[idx] = 0


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input()))
    recur(0)
    print(f"#{tc}", end=' ')
    print("Baby Gin") if bgn_result else print("Lose")