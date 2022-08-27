##import turtle
##t = turtle.Turtle()
##positions = [[0, 0, "green"], [-120, 0, "yellow"], [60, 60, "red"], [-60, 60, "black"], [-180, 60, "blue"]]
##t.pensize(5)
##
##for x, y, c in positions:
##    t.pu()
##    t.goto(x,y)
##    t.pd()
##    t.color(c, c)
##    t.circle(60)

##리스트 정리========
##리스트 생성
##리스트 =[]
##리스트 =[항목1,2,3,]: 항목들을 쉼표로 나열하여 생성
##리스트 = list()
##list1=[]
##list2=[1, 2, 3, 4]
##list3=list()
##list4=list(range(5))
##list5=list("string")
##print(list1, list2, list3, list4, list5)
##list1.append(10)
##list2.insert(2,50)
##print(list1, list2)
##list3 = list2+ list1
##print(list3)

##리스트 항목 추가
##리스트.append(): 리스트 끝에 항목 추가
##리스트.insert(인덱스, 항목): 인덱스 위치에 항목을 삽입
##리스트.extend(리스트2): 리스트 마지막에 리스트2 항목들이 추가
##+: 두 리스트를 더하여 하나의 리스트를 생성(새로운 리스트)
##주의: 두 피연산자 모두 리스트여야 함

##리스트 슬라이싱 - 문자열 슬라이싱과 동일
##리스트 항목 수정(= 인덱스와 대입 연산자 사용)
##ex) alist[5] = 5
##연속된 범위 값 수정 가능
##alist =[1,2,3,4,5,6,7,8]
##alist[2:4] = [10,20,30] # 범위로 지정하면 해당 범위의 항목들이 변경
##[1,2,[10,20,30],4,5,6,7,8]
##alist[2] => 항목(요소) 1개
##alist[2:3] => 주어진 범위만큼의(슬라이싱된, 추출된 리스트)

##리스트.remove(항목): 리스트에 있는 항목을 찾아 삭제(단, 동일한 것이 있더라도 첫 번째 것만 삭제)
##삭제할 것이 없으면 에러
##del리스트[인덱스]: 인덱스에 해당하는 항목을 삭제,del(리스트[인덱스])
##del리스트[인덱1:인덱2]: 두 인덱스(인덱스1 -(인덱2-1)) 사이에 있는 항목들을 삭제
##리스트[인덱1:인덱2] =[]
##리스트.pop(): 리스트의 맨 마지막 항목을 삭제하면서 항목을 반환
##리스트.pop(): 해당 인덱스의 위치의 항목을 삭제하면서 항목을 반환
##리스트.clear(): 리스트의 모든 항목을 삭제, del list[:], list1[:] = [], list1 = []
##주의: del list1 은 리스트 자체가 소멸

##리스트 정렬
##리스트.sort(): 정렬하는데 사용, 원본 리스트를 변경, 오름차순 정렬
##리스트.sort(reverse = True): 내림차순 정렬
##리스트.reverse(): 리스트 항목 순서를 역순으로 변경, 정렬이 아님을 주의, 원본리스트를 변경
##정렬된 새로운 리스트가 필요한 경우: sorted(리스트) 함수 사용
##ex) list2 = list1.sorted() (x), list2 = sorted(list1) (o)
##내림차순으로 정렬하려면 sorted(리스트, reverse = True)
##
##내림차순 정렬방법 추가
##리스트.sort()를 실행한 후(오름차순 정렬)
##리스트.reverse() 함수를 실행(역순으로 변경하므로 내림차순이 됨)
##
##리스트 항목 개수 세기
##리스트.count(): 리스트 내에 있는 항목의 개수를 반환
##리스트 복사
##리스트2 = 리스트.copy(): 동일 내용으로 새로운 리스트 생성
##리스트2 = 리스트 +[]
##리스트2 = 리스트[:]
##주의 리스트2 =리스트: 동일 내용으로 새로운 이름을 생성(원본리스트에 새 이름이 추가)
##
##곱 연산
##리스트를 반복(문자열 반복할 때와 동일)
##
##
##
##리스트 컴프리헨션(comprehension)
##
##alist = [ 저장항목 반복문]: 중간에 콤마가 들어가지 않고 공백이 들어감
##ex)
##alist = [random.randint(1, 10) for i in range(10)]: 10개의 랜덤 값이
##추출되어 항목ㅇ로 저장되면서 리스트 생성
##
##리스트 안의 리스트 항목(2차원 리스트)
##alist = [[0,1],[1,2], [2,3]]
##5X5 2차원 배열 만들기
##mlist = [[0]*5 for i in range(5)]
##[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

##import random
##
##rsp = ["가위", "바위", "보"]
##
##random.shufle(rsp)
##
##my_rsp = com_ rsp = "가위"
##
##while my_rsp == com_ rsp:
##    while True:
##    my_rsp = input("가위 바위 보")
##    if my_rsp in rsp:
##        break
##    else:
##        print("다시 입력")
##
##    come_rsp = random.choice(rsp)
##    if my_rsp == com_rsp:
##        print("비겼습니다. 다시 합니다.")
##    elif my rsp == "가위" and com_srp == "보" or my_srp == "바위" and com_srp
##
##
##


import random, turtle

scr = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
dice= []

for i in range(6):
    dice.append("./img/dice"+str(i+1)+"gif")
    scr.addshape(dice[i])

cnt = 1
while True:
    f_dice = random.randint(1,6)
    s_dice = random.randint(1,6)
    t.up()
    t.goto(-100,0)
    t.shape(dice[f_dice-1])
    t.stamp()
    t.goto(100,0)
    t.shape(dice[s_dice-1])
    t.stamp()

    if f_dice == s_dice:
        t.ht()
        t.goto(0,250)
        t.write("%s 만에 성공"%(cnt),False,"center",("",15,"bold"))
        break
    else:
        cnt += 1
        turtle.textinput("아쉬워라")
        
