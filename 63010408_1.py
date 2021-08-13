print("*** Rabbit & Turtle ***")
input_ = input("Enter Input : ").split()
d, Vr, Vt, Vf = [float(i) for i in input_]
ans = (d/(Vt-Vr))*Vf
print("%.2f" %ans)
