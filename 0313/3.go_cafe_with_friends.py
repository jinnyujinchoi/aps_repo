friends = ['A', 'B', 'C', 'D', 'E']
n = len(friends)
ans = 0

# 1인 bit 수를 반환하는 함수
def get_cnt(tar):
    cnt = 0
    for i in range(n):
        if tar & 0x1:   # tar가 1인지 체크하고
            cnt += 1    # 맞으면 cnt 추가
        tar >>= 1       # 그리고 밀어주기
    return cnt

# 모든 부분 집합 중 원소의 수가 2개 이상인 집합의 수
# 모든 부분집합 확인
for target in range(1<<n):
    if get_cnt(target) >= 2:
        ans += 1
print(ans)


# for i in range(1 << n):  # 0부터 31까지
#     # 현재 비트 조합에서 선택된 친구 수를 구합니다.
#     if bin(i).cnt('1') >= 2:
#         cnt += 1
#         # 선택된 친구들을 확인하고 싶다면 아래와 같이 리스트로 출력할 수 있습니다.
#         selected = [friends[j] for j in range(n) if (i >> j) & 1]
#         print(selected)
#
# print("최소 2명 이상의 친구를 선택하는 경우의 수:", cnt)
