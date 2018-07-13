PatternType = input("What pattern do you wish for??")

if PatternType == "1":
    Numberofreps = input("How many rows do you wish for?")
    Numberofreps = int(Numberofreps)
    Original = 0
    while Original <= Numberofreps:
        print(Original * "*" * 1)
        Original = Original + 1

if PatternType == "2":
    Numberofreps = input("How many rows do you wish for?")
    Numberofreps = int(Numberofreps)
    Star = "*"
    while Numberofreps > 0:
        Numberofreps = Numberofreps - 1
        print(Numberofreps * Star * 2)

if PatternType == "3":
    Numberofreps = input("How many rows do you wish for?")
    Numberofreps = int(Numberofreps)
    Original = 0
    Max = 5
    while Numberofreps > 0:
        Numberofreps = Numberofreps -1
        print(Numberofreps * "*" * 1)
        if Numberofreps = 5:
            Original = 0
            print(Original * "*" * 1)
            Original = Original + 1
