##변수 = random.choice(리스트): 리스트에 있는 항목들 중에 랜덤으로 하나의 항목을 결정하여 반환
##리스트 외에 range(), 문자열이 사용될 수 있음(시퀀스)
##변수 = random.sample(리스트, 개수): 리스트에 있는 항목들 중 랜덤으로 개수만큼 추출하여 리스트
##-> 추출 시 중복 추출은 없음
##-> 개수 입력시 리스트의 총 개수를 ㅇ초과할 수 없음
##random.shuffle(리스트): 리스트에 있는 항목들의 순서를 섞어줌. 원본 리스트를 변경


import random
##nlist = [10, 45, 28, 91, 84, 77, 56]
##n = random.choice(nlist)
##print(n)
##n2 = random.sample(nlist, 2)
##print(n2)
##n3 = random.sample(nlist, 7)
##random.shuffle(nlist)
##print(nlist)

##
##dolist = []
##for i in range(5):
##    do1 = input("해야 할 일(%s): "%(i+1))
##    dolist.append(do1)
##
##random.shuffle(dolist)
##n1 = random.choice(dolist)
##n2 = random.sample(dolist, 2)
##print(n1)
##print(n2)


my = []

for i in range(5):
    my1 = input("띵언 입력:")
    my.append(my1)

dailymy = random.choice(my)

print("#"*15)
print(" 오늘의 명언")
print("#"*15)
print("")
print(dailymy)
