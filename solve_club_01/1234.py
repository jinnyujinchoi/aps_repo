# 비밀번호 구하기 함수
def password(arr, N):
    s = []          # 스택 생성
    for num in arr: # 배열 안 문자 순회
        # 스택이 비어있지 않고, 마지막 요소가 현재 num과 같다면
        if s and s[-1] == num:
            s.pop()     # 마지막 요소 제거
        else:
            s.append(num)   # 아니면 스택에 어펜드
    return "".join(map(str, s))   # 문자열로 변환해서 반환

for tc in range(1, 11):
    N, num = input().split()
    N = int(N)
    num_lst = list(map(int, num))
    print(f"#{tc} {password(num_lst, N)}")