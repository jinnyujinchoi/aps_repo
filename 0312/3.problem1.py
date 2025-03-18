# 주사위 3개를 던져 합이 10이하인 경우는 몇 개인가?
# 종료조건 : 3번 던짐
# 나올 범위 : 주사위는 1~6

path  = []
result = 0

def recur(cnt, total):
    global result
    # 기저조건 쳐내주기(가지치기)
    if total > 10:
        return

    if cnt == 3:
        # 합이 10 이하인건 몇 개?
        # if path의 합이 10 이하라면? result += 1이 되겠지?!
        # sum: path 길이만큼 반복되기 때문에 비효율
        if total <= 10:
            result += 1
            print(path)
        return

    for num in range(1, 7):
        path.append(num)
        recur(cnt+1, total+num)     # 주사위 결과를 더해서 전달
        path.pop()

recur(0, 0)