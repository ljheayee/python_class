##
##import random
##list1 = ["치약", "샴푸", "린스", "주방세제", "키친타올", "칫솔"]
##
##mul = input("새로 구매할 물품 입력")
##
##i = random.randrange(len(list1))
##
##list1.insert(i, mul)
##
##for j in range(len(list1)-1):
##    if list1[j] == mul:
##        list1.remove(list1[j])
##print(list1)
##mul = input("새로 구매할 물품 입력")
##
##if mul in list1:
##    print("%s는 %s번째에 있다"%(mul, list1.index(mul)+1))
##
##
##list1.sort(reverse = True)
##
##print(list1)
##print("마지막 구매 물품: %s"%(list1.pop()))
##print(list1)
##
##
##
##import random
##exam1 = [random.randint(50,100) for i in range(7)]
##exam2 = [random.randint(50,100) for j in range(7)]
## 
##print(exam1)
##print(exam2)
##print(exam1[1])
##
##for k in range(6):
##    if exam1[k] >= 70 and exam2[k] >= 70:
##        print("승진대상 %s번"%(exam1.index(exam1[k])+1))
##
##
##
##def get_sum(start, end):
##    sum1 = 0
##    for i in range(start, end+1):
##        sum1 += i
##    print("sum=", sum1)
##
##get_sum(1,10)
##get_sum(1,20)
##
##
##
##def calculate_area(radius):
##    area = 3.14*radius**2
##    return area
##
##c_area = calculate_area(5.0)
##print(c_area)
##
##area_sum = calculate_area(5.0) + calculate_area(10.0)
##
##print(area_sum)
import random

def random_save(nlist, num, minn, maxn):
    for i in range(num):
        num_list.append(random.randint(minn, maxn))
##    nlist = [random.randint(minn,maxn) for i in range(num)]

def list_print(nlist):
    for i in range(len(nlist)):
        print("%4s"%(nlist[i]), end ="")
        if (i+1)% 10 == 0:
            print()

def sum_and_avg(nlist):
    nsum = 0
    for i in nlist:
        nsum +=i
        avg = nsum/len(nlist)
        return nsum, avg
num_list = []
random_save(20, 1, 100)
list_print(num_list)
nsum, avg = sum_and_avg(num_list)
print("합: %s, 평균: %.2f"%(nsum, avg))
