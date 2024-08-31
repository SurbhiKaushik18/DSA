a=int(input("Enter the number: "))
if a<2:
    print("The number you entered is not prime.")
elif a>=2:
    for i in range(2,a):
        if a%i==0:
            print("Number is not prime.")
            break
    else:
        print("Prime Number")