n = int(input())

temp = n
sum_fact = 0

while temp > 0:
    digit = temp % 10

    # factorial of digit
    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    sum_fact += fact
    temp = temp // 10

if sum_fact == n:
    print("Strong Number")
else:
    print("Not Strong Number")