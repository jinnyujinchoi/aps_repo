'''
1차원 배열 - N일 동안의 매매가
최대한 많이 구입해서 매매가가 높은 날에 제일 많이 팔자!
판매는 언제든 가능!
그렇다면 매매가가 싼 날에만 구입!(1만 구입 가능)
매매가가 높은 날에 제일 많이 판매 - 판매는 매매가 높은 날에 몰빵
----------------------------문제 예예
안사도 되는 케이스
첫 날이 고점이면 살 필요가 없다.
그 외에는?
뒤에 작은값이 나오기 전이 고점!
고점 기준으로 앞의 값 차익 더하기
뒤로 반복
'''

def solve(chart, N):
    pf = 0                      # 차익 초기화
    max_v = chart[N-1]          # 뒤에서부터 봤을 때 최댓값 초기화
    for i in range(N-2, -1, -1):
        if chart[i] < max_v:
            pf += max_v - chart[i]
        else:
            max_v = chart[i]
    return pf


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    chart = list(map(int, input().split()))
    print(f"#{tc} {solve(chart, N)}")
