def solve(A, B):
    C = []
    i = j = 0
    while i+j < N+M:
        if i < N:
            if A[i]:
                C.append(A[i])
                i += 1
        if j < M:
            if B[j]:
                C.append(B[j])
                j += 1

    return C


T = int(input())
for tc in range(1, T+1):
    N, M= map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(f"#{tc}", *(solve(A, B)))