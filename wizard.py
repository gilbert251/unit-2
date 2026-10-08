def wizard(owner, num, duels):

    unique_owners = {owner}
    for i in range(num):
        if duels[i][1] == owner:
            owner = duels[i][0]
            unique_owners.add(owner)
    print(f"{owner}{len (unique_owners)}")

wizard("X", 4, ["AX", "BX", "XA", "DA"])

