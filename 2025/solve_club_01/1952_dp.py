T = int(input())
for tc in range(1, T+1):
    c_day, c_month, c_month3, c_year = map(int, input().split())
    days = [0] + list(map(int, input().split()))

    dp = [0]*13
    dp[1] = min(days[1] * c_day, c_month)
    dp[2] = dp[1] + min(days[2] * c_day, c_month)

    for month in range(3, 13):
        # N월의 최소 비용 후보
        # 1. (N-3)월에 3개월 이용권 구입한 경우
        # 2. (N-1)월에 최소 비용 + 1일권 구매
        # 3. (N-1)월의 최소 비용 + 1달권 구매
        dp[month] = min(dp[month-3] + c_month3,
                        dp[month-1] + (days[month] * c_day),
                        dp[month-1] + c_month)
    # 12월의 최소 누적 금액 vs 1년권
    ans = min(dp[12], c_year)
    print(f"#{tc} {ans}")