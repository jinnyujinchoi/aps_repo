def f(n):
    global left, right
    if node[n] in '+-*/':
        l = f(left[n])
        r = f(right[n])
        if node[n] == '+':
            return l+r
        elif node[n] == '-':
            return l-r
        elif node[n] == '*':
            return l*r
        else:
            return l/r
    else:
        return int(node[n])

for tc in range(1, 11):
    N = int(input())

    node = [0]*(N+1)
    left = [0]*(N+1)
    right = [0]*(N+1)

    for _ in range(N):
        n, *arr = input().split()
        node[int(n)] = arr[0]
        if arr[0] in '+-*/':
            left[int(n)] = int(arr[1])
            right[int(n)] = int(arr[2])

    result = f(1)
    print(f"#{tc} {int(result)}")