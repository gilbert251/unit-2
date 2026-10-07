def wizard(owner, num, duels):

    num_owners= 1
    for i in range(num):
        if duels[i][1] == owner:
            owner = duels[i][0]
            num_owners += 1
    print(owner, num_owners)

wizard("X", 4, ["AX", "BX", "XA", "DA"])

