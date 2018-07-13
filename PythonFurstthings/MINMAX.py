def MINMAX():
    Numbers = []
    active == True
    while active == True:
        i = int(input("Enter number"))
        h = input("To stop enter 'stop. To continue enter 'Continue'")
        Numbers.append(i)
        if h == 'Stop':
            active = False
        elif h == 'Continue':
            active = True
            ha = sorted(Numbers)
            print(ha)
            print("min = " + str(ha[0]))
            print("max = " + str(ha[-1]))
