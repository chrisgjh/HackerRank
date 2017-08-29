import math
num = int(input())
x = [int(i) for i in input().split(' ')]
mean = sum(x)/num
total = 0
for i in range(num):
    total += (x[i]-mean)**2
std = math.sqrt(total/num)
print("{:.1f}".format(std))