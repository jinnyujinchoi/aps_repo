'''
구현 단계
사탕을 담은 상자
- A, B, C 개
- 순증가하길 원한다.
- 각 상자에는 1개 이상의 사탕이 들어있어야 한다.

목표
- 순증가하도록 만들자
- 0개 이상을 먹자

설계
- 두 번째 상자
    - 세 번째 상자보다 작게 만들자
- 첫 번째 상자
    - 두 번째 상자보다 작게 만들자
-------------------문제 읽기 단계

- 자료구조
- 3개의 숫자 + 먹은 개수 만 저장하면 끝
- 리스트 vs A,B,C 저장

- 알고리즘
- B는 C 보다 작아야 한다
- B를 C보다 작을 때 까지 하나씩 감소
[검증]
사탕의 개수가 많으면, 시간 초과 가능성
    - 300 까지니 가능하다.
    - B가 C보다 크다면, B = C-1로 만들어준다.
--------------------설계 단계
'''
def solve(a, b, c):
    eat = 0  # 먹은 사탕 개수 저장
    # 조건을 만족하지 못하는 경우
    if b < 2 or c < 3:
        return -1

    # 조건 만족 시, 사탕 먹기
    if b >= c:
        eat += b - (c - 1)
        b = c - 1

    if a >= b:
        eat += a - (b - 1)
        a += b - 1

    return eat

T = int(input())
for tc in range(1, T+1):
    one, two, three = map(int, input().split())
    print(f"#{tc} {solve(one, two, three)}")

