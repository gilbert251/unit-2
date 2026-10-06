def wizard(owner, num, duels):

    owner_amount = 1
    owner=owner
    num_owners= 1
    for i in range(num):
        if duels[i][0] == owner:
            owner = duels[i][0]
            num_owners += 1
    print(owner, num_owners)

wizard("A", 3, ["BA", "CB", "DA"])

