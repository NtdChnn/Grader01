num = input()
num = int(num)
for i in range(0, num):
    for x in range(i, num-1):
        print(".", end="")
    print("*", end="")
    for y in range(0, (i*2)-1):
        print("+", end="")
    if i != 0:
        print("*", end="")
    for x in range(2*i, (2*(num-1))-1):
        print(".", end="")
    if i != num-1:
        print("*", end="")
    for y in range(0, (i*2)-1):
        print("+", end="")
    if i != 0:
        print("*", end="")
    for x in range(i, num - 1):
        print(".", end="")
    print("")
for i in range(0, (num*2)-2):
    for x in range(0, i+1):
        print(".", end="")
    print("*", end="")
    for x in range(i*2, (num*4)-7):
        print("+", end="")
    if i != (num*2)-3:
        print("*", end="")
    for x in range(0, i+1):
        print(".", end="")
    print("")
