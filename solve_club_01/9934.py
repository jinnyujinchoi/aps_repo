def container(goods, truck):
    goods.sort(reverse=True)
    truck.sort(reverse=True)
    used = [False] * len(goods)
    total = 0
    t = 0
    while t < M:
        g = 0
        while g < N:
            if not used[g] and goods[g] <= truck[t]:
                total += goods[g]
                used[g] = True
                break
            g += 1
        t += 1
    return total

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    goods = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    print(f"#{tc} {container(goods, truck)}")