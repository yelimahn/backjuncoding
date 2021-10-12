a=int(input())
b=int(input())
c=int(input())

output=a*b*c
count=str(output)
for i in range(10):
    print(count.count(str(i)))