print("*** multiplication or sum ***")
num1_s, num2_s = input("Enter num1 num2 : ").split()
num1 = int(num1_s)
num2 = int(num2_s)
print("The result is", end=" ")
if num1*num2 > 1000:
    print(num1+num2)
else:
    print(num1*num2)
