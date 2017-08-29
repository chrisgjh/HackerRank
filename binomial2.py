from math import factorial

def combination(n, x):
    return (factorial(n) / (factorial(x) * factorial(n - x)))

def binomial(n, x, p, q):
    answer = combination(n, x)
    answer *= (p ** x)
    answer *= (q ** (n - x))
    return answer

s = [int(i) for i in input().split()]
p = s[0] / 100
q = 1 - p

prob = 0
for i in range(0, 3):
    prob += binomial(10, i, p, q)

print(round(prob, 3))

prob = 0
for i in range(2, 11):
    prob += binomial(10, i, p, q)
print(round(prob, 3))