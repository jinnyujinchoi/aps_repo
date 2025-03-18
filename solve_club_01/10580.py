'''
전선 N개
- 교차점 발생
- 몇 개 발생하는 지 COUNT
----------------------문제 읽기

교차점은 무슨 조건일 때 발생할까?

발생하는 조건 두 가지
- 새로운 선을 추가할 때
    - 기존 선과 비교 (다 1000번 이라고 가정해도ㅇㅋ)
        -> 기존선 들을 저장하면서 진행
        - 1. 시작점이 높으며, 도착점이 낮음
        - 2. 시작점이 낮으며, 도착점이 높음
----------------------설계
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())

    wires = []
    cnt = 0

    for _ in range(N):
        s, e = map(int, input().split())

        for p_s, p_e in wires:
            if s < p_s and e > p_e:
                cnt += 1
            if s > p_s and e < p_e:
                cnt += 1

        wires.append([s, e])
    print(f"#{tc} {cnt}")
