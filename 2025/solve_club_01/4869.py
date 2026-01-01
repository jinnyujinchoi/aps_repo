def paper(N):     # 종류 개수 배열
    f = [0] * (N//10 + 1)
    f[0] = 1
    f[1] = 1
    for i in range(2, N//10+1):
        f[i] = f[i-1] + 2*(f[i-2])

    return f[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f"#{tc} {paper(N)}")