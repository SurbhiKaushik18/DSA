n=int(input("Enter the number: "))
num=1
for row in range(1,n+1):
    for col in range(1,n+1):
        print(num, end=" ")
        num=num+1
    print()