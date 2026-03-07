# 짝수 개수는 y부터, 홀수 개수는 x부터
# 더해야 할 값: row
N = int(input())
row, end = 1, 1
# 행 찾기
while end < N:
    row += 1
    end += row
# 그 수가, 행의 첫 번째 값으로부터 얼마나 떨어져 있는지
start = end - row + 1
d = N - start # 더할 값
# 시작점 찾고, 분수 찾기
if row%2 == 0:
    x, y = 1, row
    x += d
    y -= d
else:
    x, y = row, 1
    x -= d
    y += d

print(f'{x}/{y}')