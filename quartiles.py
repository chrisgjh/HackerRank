from statistics import median
num = int(input())
x = sorted([int(i) for i in input().split(' ')])
q2 = int(median(x))
if (num % 2 != 0):
    q1 = median(x[:num//2])
    q3 = median(x[num//2+1:])
else:
    q1 = median(x[:num//2+1])
    q3 = median(x[num//2:])
print(int(q1))
print(q2)
print(int(q3))