# 학번: 2011521096 이름: 이재혁

jumsu1 = int(input("1차 점수를 입력하세요.: ")) # 1차 점수 입력
jumsu2 = int(input("2차 점수를 입력하세요.: ")) # 2차 점수 입력

avg = (jumsu1+jumsu2)/2 #점수 평균 변수 작성

if jumsu1 >100 or jumsu2 >100 or jumsu1<0 or jumsu2<0: #점수가 100점 만점으로 생각 그외의 점수는 잘 못 입력한 것으로 나타냄
    print("점수를 잘 못 입력하셨습니다.")
    
elif avg >=70 or (jumsu1 >= 60 and jumsu2 >=60): #평균이 70점 이상이거나 각 점수가 60점 이상 되도록 조건문 
    print("승진이 가능합니다")

else:
    print("승진이 불가능합니다") # 나머지 경우는 평균이 70이 안되거나 평균 점수가 60이 안되는 경우
