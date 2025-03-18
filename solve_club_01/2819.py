import sys
sys.stdin = open("sample_input (18).txt", "r")

# 접근법
# 시작 지점 : 전체 다 보아야 함
# 재귀 돌리면서(상하좌우 이동) 숫자를 붙인다
# 숫자가 7자리가 되면, set에 넣는다(중복제거)
def recur(i, j, number):
    if len(number) == 7:
        result.add(number)
        return

    for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
        ni, nj = i+di, j+dj
        if 0<=ni<4 and 0<=nj<4:
            # 다음 위치 추가하는 코드
            recur(ni, nj, number + matrix[ni][nj])


T = int(input())
for tc in range(1, T+1):
    matrix = [input().split() for _ in range(4)]
    result = set()

    for i in range(4):
        for j in range(4):
            recur(i, j, matrix[i][j])

    print(f"#{tc} {len(result)}")