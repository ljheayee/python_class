import random
classdic = {}

for i in range(34):
    classdic["stud"+str(i)] = [random.randint(0,100) for i in range(3)]
print(classdic)

print(classdic.keys())
avg = []
for i in range(34):
    if i in classdic.values():
        avg.append(max((i[0]+i[1]+i[2])/3))
print("평균이 가장 높은 학생의 평균은%s"%avg)
