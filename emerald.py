def maxemerald(num,wieghts):
    list = []
    testnum = 0
    for i in range(num):
        if weights[i] % 2 == 0:
            testnum += weights[i]
        else:
            list.append(testnum)
            testnum=0
    maxnum=max(list)
    print(maxnum)
