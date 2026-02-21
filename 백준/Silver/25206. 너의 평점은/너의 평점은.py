score_num = 0 # 총 학점
score_sum = 0 # 총 합계
# 평점 딕셔너리
score = {'A+': 4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0,
       'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

for _ in range(20):
    info = input().split()
    if info[2] == 'P': # pass면 통과
        continue
    score_num += float(info[1])
    score_sum += float(info[1]) * score[info[2]]

ans = score_sum / score_num
print(ans)