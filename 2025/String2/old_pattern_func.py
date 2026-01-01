def bruteforce(p, t):
    N = len(t)
    M = len(p)
    i = j = 0
    while i < N and j < M:
        if t[i] != p[j]:  # 두 원소 다르면
            i = i - j + 1  # i-j 비교를 시작했던 위치
            j = 0
        else:  # 원소 같으면
            i += 1
            j += 1
    if j == M:  # 패턴의 끝까지 가면!
        return i-j  # 시작 위치 반환
    else:
        return -1   # 패턴이 없는 경우

t = 'TTTTTATTAATA'
p = 'ATA'
print(bruteforce(p, t))