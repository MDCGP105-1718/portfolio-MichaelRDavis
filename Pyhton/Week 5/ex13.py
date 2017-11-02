def remove_dups(L1, L2):
    for e in range(0,4):
        if e in L2:
            print(e)
            L1.remove(e)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups(L1, L2)
