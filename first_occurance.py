n=int(input())
n2=list(map(int, input().split()))
n3=int(input())
found=-1
for i in range(n):
    if n2[i]==n3:
        found=i
        break
print(found)

