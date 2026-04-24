n=int(input("enter range:"))
dict1={}
dict2={}
print("enter the first:")
for i in range(n):
    key1=input()
    value1=input()
    dict1[key1]=value1
print("enter the second:")
for i in range(n):
    key2=input()
    value2=input()
    dict2[key2]=value2


for key in dict1:
    if key in dict2:
        if dict1[key] != dict2[key]:
            print(key)
    else:
        print(key)

