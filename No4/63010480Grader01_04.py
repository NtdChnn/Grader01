def odd_list(al):
    ans = []
    for x in al:
        if x % 2 == 1:
            ans.append(x)
    return ans

print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)
