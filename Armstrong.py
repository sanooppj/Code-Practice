n = int(input())

temp = n
digits = len(str(n))
sum_val = 0

while temp > 0:
    digit = temp % 10
    sum_val += digit ** digits
    temp = temp // 10

if sum_val == n:
    print("YES")
else:
    print("NO")