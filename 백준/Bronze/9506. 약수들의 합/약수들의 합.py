while 1:
    N = int(input())
    arr = []
    if N == -1:
        break

    for i in range(1, int(N ** 0.5)+1):
        if N % i == 0:
            arr.append(i)
            if i != N // i:
                arr.append(N // i)
    arr.sort()
    proper = [d for d in arr if d != N]

    if sum(proper) == N:
        print(f'{N} = ' + ' + '.join(map(str, proper)))
    else:
        print(f'{N} is NOT perfect.')