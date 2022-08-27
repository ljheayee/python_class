#학번: 201521096, 이름: 이재혁

import random

allscore = [] #전체 학생 점수 리스트 생성
avg = [] #학생 평균 리스트 생성

print("*"*15)
print("학생들 점수 목록")

for i in range(32):
    kor = random.randint(30,100)
    eng = random.randint(30,100)
    math = random.randint(30,100)
    score = [kor, eng, math] #스코어리스트를 생성
    allscore.append(score) #생성된 스코어를 allscore 리스트에 추가
    avg.append((kor+eng+math)/3)  #생성된 3개의 평균 합을 avg에 추가
    
print(allscore) #전체 학생들 점수 목록 출력

print("*"*15)
print("평균이 최고인 학생")


for m in range(0,31): #리스트 중 평균이 최대인 평균과 같을시 출력하는 형태로
    if avg[m] == max(avg):
        print("%s : %s(avg: %s)"%(m+1, allscore[m], "%.2f"%avg[m]))
        # 번호는 1부터 시작하기 때문에 m+1, 전체학생 리스트중 m번째 출력, 평균은 둘 째짜리까지 출력                        
print("*"*15)

k = random.randint(5,10) #5 - 10명 샘플 생성
print("%s명 학생 샘플"%k)

for w in range(k): #양식에 맞게 점수와 평균 추가
    x = random.randint(0,31)
    print("%s(avg: %s)"%(allscore[x], "%.2f"%avg[x]))


#for in in samavg:
    #sum1 = i[0] + i[1] + i[2]
    #avg =sum1/3
    #
