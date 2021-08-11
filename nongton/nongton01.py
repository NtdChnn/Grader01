input_ = input().split()
input_ = [int(i) for i in input_]
count = int(0)
countdown = []
anslist = []
for i in range(0, len(input_)):
    if i != 0:
        if input_[i] == input_[i-1]-1:
            countdown.append(input_[i-1])
        else:
            countdown.clear()
    if input_[i] == 1:
        count += 1
        countdown.append(1)
        anslist.append(countdown.copy())
        countdown.clear()
anslist.insert(0, count)
print(anslist)
