allBid = input("Enter All Bid : ").split()
if len(allBid) == 1:
    print("not enough bidder")
allBid = [int(i) for i in allBid]
allBid.sort(reverse=True)
if allBid[0] == allBid[1]:
    print("error : have more than one highest bid")
else:
    print("winner bid is {} need to pay {}".format(allBid[0], allBid[1]))
