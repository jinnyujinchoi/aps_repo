def f(n):
    global l, r
    if node[n] in '+-*/':
        l = f(l[n])
        r = f(r[n])
        if node[n] == '+':
            return r+l
        elif node[n] == '-':
            return r-l
        elif node[n] == '*':
            return r*l
        else:
            return r/l
    else:
        return int(node[n])

for tc in range(1, 11):
    N = int(input())

    node = [0]*(N+1)
    l = [0]*(N+1)
    r = [0]*(N+1)

    for _ in range(N):
        n, *arr = input().split()
        node[int(n)] = arr[0]
        if arr[0] in '+-*/':
            l[int(n)] = int(arr[1])
            r[int(n)] = int(arr[2])

    result = f(1)
    print(f"#{tc} {int(result)}")