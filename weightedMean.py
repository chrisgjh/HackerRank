num = int(input())
x = [int(i) for i in input().split(' ')]
w = [int(i) for i in input().split(' ')]
total = sum([x[i] * w[i] for i in range(num)])
print("{:.1f}".format(total/sum(w)))