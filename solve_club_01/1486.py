import sys
sys.stdin = open("input (31).txt", "r")

# level : 점원 수
# branch : 탑에 포함 시킬까 말까
def recur(cnt, total_h):
    global ans
    # 기저조건 가지치기
    # 이미 B이상 이면, 점원 더 쌓을 필요x
    if total_h >= B:
        ans = min(ans, total_h)
        return

    if cnt == N:
        return

    recur(cnt + 1, total_h + heights[cnt])      # 포함 시키는 경우
    recur(cnt + 1, total_h)      # 포함 노 경우

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    ans = 200001
    recur(0,0)
    print(f"#{tc} {ans-B}")
