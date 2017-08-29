s = [int(i) for i in input().split()]
p = s[0] / s[1]
first_detect = int(input())

prob = p*(1-p)**(first_detect-1)

print(round(prob, 3))