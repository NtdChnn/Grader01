print("*** Rabbit & Turtle ***")
d, Vr, Vt, Vf = input("Enter Input : ").split()
D = float(d)
VR = float(Vr)
VT = float(Vt)
VF = float(Vf)
t = float(D/(VT-VR))
ans = t*VF
print("%.2f" %ans)
