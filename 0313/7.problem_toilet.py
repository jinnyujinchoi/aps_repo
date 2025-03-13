people = [15, 30, 50, 10]
n = len(people)

# 접근법, 최소 시간인 사람부터 화장실로 들어가자
people.sort()   # 오름차순 정렬

total_time = 0      # 전체 대기 시간
waiting_p = n-1   # 대기인원 수

for turn in range(n):
    time = people[turn]
    total_time += time*waiting_p
    waiting_p -= 1

print(total_time)