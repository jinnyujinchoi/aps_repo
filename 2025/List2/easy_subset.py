arr = [3,6,7,1,5,4]
n= len(arr) # 원소의 개수

# 리스트로 출력하기
for i in range(1<<n):   # 1<<n : 부분 집합의 개수
    sub_lst = []
    for j in range(n):  # 원소의 수만큼 비트 비교
        if i & (1<<j):  # i의 j번 비트가 1인 경우
            sub_lst.append(arr[j])  # j번 원소 출력

    print(sub_lst)
# 쌩으로 출력하기
# for i in range(1<<n):   # 1<<n : 부분 집합의 개수
#     for j in range(n):  # 원소의 수만큼 비트 비교
#         if i & (1<<j):  # i의 j번 비트가 1인 경우
#             print(arr[j], end=", ")
#     print()
# print()