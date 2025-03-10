'''
값이 0인 복도 배열을 만들고
지나가면 1을 해준 다음, max 값을 찾자!
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    corridor = [0]*200
    for _ in range(N):
        s, e = map(int, input().split())
        if s > e:
            s_i = (e - 1) // 2
            e_i = ((s - 1) // 2)
        else:
            s_i = ((s - 1) // 2)
            e_i = (e - 1) // 2
        for i in range(s_i, e_i+1):
            corridor[i] += 1

    ans = max(corridor)
    print(f"#{tc} {ans}")