# 베이비진 검증 / 승자 반환
def babygin(arr, winner):
    cnt = 0     # 카운팅 배열 안 연속 횟수 검증(triplet)
    for num in arr:
        if num:
            cnt += 1    # 배열 안에 값 있으면 1
        else:
            cnt = 0     # 없으면 0으로 초기화
       # run이 성립하거나 triplet이 성립하거나
        if cnt == 3 or num == 3:
            return winner
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    p1 = [0]*10         # player1의 카운팅배열
    p2 = [0]*10         # player2의 카운팅배열
    card = list(map(int, input().split()))
    for i, x in enumerate(card):
        if i % 2:
            p2[x] += 1
            ans = babygin(p2, 2)    # player2의 결과 검증
        else:
            p1[x] += 1
            ans = babygin(p1, 1)    # player1의 결과 검증
        if ans:
            break
    print(f"# {tc} {ans}")



