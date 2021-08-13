input_ = [int(i) for i in input().split()]
countdown = []
anslist = [0]
for i in range(0, len(input_)):
    if i != 0:
        countdown.append(input_[i-1]) if input_[i] == input_[i-1]-1 else countdown.clear()
    if input_[i] == 1:
        anslist[0] += 1
        countdown.append(1)
        anslist.append(countdown.copy())
        countdown.clear()
print(anslist)
