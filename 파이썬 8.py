##slist = ["영어", "수학", "사회", "과학"]
##print(slist)
##print(slist[0])
##
##cart = []
##cart.append("샴푸")
##print(cart)
##cart.append("비누")
##print(cart)
##print(cart[0])
##
##
##for i in slist:
##    print(i)
##
##for i in range(len(slist)):
##    print(slist[i])
##
##
##cart = ["사과","세제", "화장지", "치약"]
##cart[1] = "섬유유연제"
##print(cart)
##cart.append("양말")
##print(cart)
##cart.insert(1, "건전지")
##print(cart)
####cart.insert(7, "린스")
##cart.insert(len(cart), "린스")
##print(cart)
##
##

##num = [[10, 20, 30, 45], [ 40, 50, 60], ["a", "b", "c"]]
##
##print(num[2])



dolist = []
for i in range(5):
    do1 = input("해야 할 일 입력(%s): "%(i+1))
    dolist.append(do1)
print(dolist)

while True:
    n = int(input("인덱스 값 입력:"))
    if n >= 0 and n < len(dolist):
        print("선택한 일은 %s"%(dolist[n]))
        break
    else:
        print(" 잘못입력하셨습니다")

