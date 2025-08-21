#  Check the largest and smallest of three numbers
print("Enter three numbers:")
num1 = int(input("Number 1: ")) 
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))
if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest number")
    if num2 <= num3:
        print(f"{num2} is the smallest number")
    else:
        print(f"{num3} is the smallest number") 
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the largest number")
    if num1 <= num3:
        print(f"{num1} is the smallest number")
    else:
        print(f"{num3} is the smallest number")
elif num3 >= num1 and num3 >= num2:
    print(f"{num3} is the largest number")
    if num1 <= num2:
        print(f"{num1} is the smallest number")
    else:
        print(f"{num2} is the smallest number")
else:
    print("All numbers are equal")