A, B = map(int, input().split())
# a1 = A+B
# a2 = A-B
# a3 = A*B
# a4 = A%B
# print(a1)
# print(a2)
# print(a3)
# print(a4)

ans = [A+B, A-B, A*B, A//B, A%B]
print(*ans, sep="\n")
# *() -> 언패킹
# sep= -> 구분자 넣기