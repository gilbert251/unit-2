def spaces(h,y,z):
    john = 0
    ham = list(y)
    yes = list(z)
    for i in range (h):
        k = yes[i]
        a = ham[i]
        if k and a == "C":
            john = john + 1
    print(john)

spaces(5, "CC.C")
