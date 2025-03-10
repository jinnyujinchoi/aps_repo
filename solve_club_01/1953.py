'''
지도 - 2차원 배열
맨홀 뚜껑으로부터 출발
1. BFS로 접근
    - 이동 방향 : 상하좌우
    - 이동이 불가능한 케이스
        - [델타 배열 기본] 범위 밖으로 나가면 못감
        - [방문 기록 기본] 이미 방문한 곳은 안감
        - [문제 조건]
            - 현재 내 위치에서 뚫려있는 곳으로만 이동 가능
            - 다음 가려는 곳의 터널이 뚫려 있는 곳으로만 이동 가능
            -> 이런 케이스는 델타 배열 순서와 동일하게,
                    이동 가능 여부를 기록해 두면 좋다.
2. 방문 기록을 해야 한다 (visited)
--------------------------------------문제 읽기

이차원 리스트 형태 + 미로 탐색 문제 유형
- 우리가 배운 알고리즘 종류 (DFS, BFS)
    - 일단 끝까지 가보자 (DFS)
        - 재귀호출이 최악의 경우 2500번 발생 가능
        - 파이썬의 재귀 호출 기본 제한은 1,000번
    - 주변으로 퍼져나가면서 확인하자 (BFS)
        - 이 문제는 BFS로 푸는게 쉽겠구나

- BFS
    - Queue를 활용해서 먼저 방문한 노드부터 탐색 시작
        - 먼저 방문한 노드에서 갈 수 있는 노드들을 후보군에 추가가

- BFS 시간복잡도
    - 0(V+E)
        - V: 정점의 개수 / E: 간선의 개수
        - 정점의 개수 = 2,500 개
        - 간선의 개수 = 2500*4 = 10,000 개

---------------------------------자료구조, 알고리즘 설계
'''

