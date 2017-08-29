from statistics import median
num = int(input())
final = []
x = [int(i) for i in input().split(' ')]
f = [int(i) for i in input().split(' ')]
j = 0
k = 0
while j < len(f):
    for i in range(0, f[j]):
        final.append(x[j])
    j += 1
final = sorted([int(i) for i in final])
if len(final) % 2 == 0:
    q1 = median(final[:len(final)//2])
    q3 = median(final[len(final)//2:])
    print(float(q3 - q1))
else:
    q1 = median(final[:len(final)//2-1])
    q3 = median(final[len(final)//2+1:])
    print(float(q3 - q1))