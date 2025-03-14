import sys
sys.stdin = open("sample_input (19).txt", "r")

# 완전 탐색을 하는 버전
# 각 달에 4가지 케이스를 모두 확인하면서 진행
def recur(m, c_total):
    global min_ans
    # 가지치기
    if min_ans < c_total:
        return

    if m > 12:
        min_ans = min(min_ans, c_total)
        return

    # 1일 이용권으로 다 사는 경우
    recur(m+1, c_total+(days[m] * c_day))
    # 1달 이용권으로 다 사는 경우
    recur(m+1, c_total+c_month)
    # 3달 이용권으로 다 사는 경우
    recur(m+3, c_total+c_month3)
    # 1년 이용권으로 다 사는 경우
    recur(m+12, c_total+c_year)

T = int(input())
for tc in range(1, T+1):
    # 이용권 가격들
    c_day, c_month, c_month3, c_year = map(int, input().split())
    # 12개월 이용계획
    days = [0] + list(map(int, input().split()))    # 0월 버리기
    min_ans = int(21e8)
    recur(1, 0)
    print(f"#{tc} {min_ans}")