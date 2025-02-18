def f(i, N, s, t, rs):  # i원소, N 집합의 크기, s i-1까지 고려된 합, t목표
    global cnt
    global fcnt
    fcnt += 1
    if s == t:   # 고려한 원소의 합이 찾는 합보다 큰경우(가지치기)
        print(bit, s)
        cnt += 1  # 부분집합 찾았으므로 +1
    # 바로 이 코드가 가지치기의 효과!
    # 이 한줄만 추가해줘도 횟수가 훨 줄어듬!!
    elif s > t:    # 정답을 찾은 경우! 원소합이 목표값일 때!
        return  # 합이 목표를 초과하면 더 탐색할 필요x
    elif i == N:    # 모든원소를 고려했는데도 없다면 종료
        return
    elif s + rs < t:
        return      # 남은 원소를 다 더해도 찾을 수 없으면
    else:
        bit[i] = 1
        f(i+1, N, s+A[i], t, rs-A[i])    # A[i] 포함
        bit[i] = 0
        f(i+1, N, s, t, rs-A[i])         # A[i] 미포함

A = [1,2,3,4,5,6,7,8,9,10]
# N = 10
# A = [ i for i in range(1, N+1)]

rs = 0
key = 55    # 목표 값
cnt = 0     # 목표값 찾은 횟수! / 부분집합 개수
bit = [0]*len(A)  # bit 연산자 담을 리스트
fcnt = 0    # 함수 호출 횟수
f(0, len(A), 0, 1, rs)
print(cnt, fcnt)      # 합이 key인 부분집합의 수