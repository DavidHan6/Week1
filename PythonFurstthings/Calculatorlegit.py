Mode = input("What would you like to do?")

def BMIcalculator():
    Unit = input("Metric or Customary/Imperial ")

    if Unit == "Metric":
        hight = input("Please enter hight in meters ")
        weight = input("Please enter weight in kilos ")
        hight = float(hight)
        weight = float(weight)
        BMI = weight/hight**2

    if Unit == "Customary/Imperial":
        hight = intput("Please enter hight in Feet and Inches")
        weight = input("Please enter weight in pounds")
        hight = float(hightss)
        weight = float(weight)
        BMI = 703*weight/hight**2

    print(str(BMI))
    if BMI > 20 and BMI < 25:
        print("Healthy")
    if BMI < 20:
        print("underweight")
    if BMI > 25:
        print("OBESE")

def Addition(a, b):
    Answer = a + b
    return Answer

def Subtraction(a, b):
    Answer = a - b
    return Answer

def Multiplication(a, b):
    result = a * b
    return result

def Division(a, b):
    result = a / b
    return result

def Exponents(a, b):
    Answer = a**b
    return Answer

def MinMax(a, b):
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

def Hangman():
    import random
    def FullHangman():
        print("                                                                      ")
        print("    ╔══════════════════════════════════╤══                            ")
        print("    ║        /                         │                              ")
        print("    ║       /                          │                              ")
        print("    ║      /                           │                              ")
        print("    ║     /                            │                              ")
        print("    ║    /                         _________                          ")
        print("    ║   /                        /           \                        ")
        print("    ║  /                        |     ○   ○   |                       ")
        print("    ║ /                         |             |                       ")
        print("    ║/                          |             |                       ")
        print("    ║                            \    ────   /                        ")
        print("    ║                              ─────────                          ")
        print("    ║                       __________╟──╢__________                  ")
        print("    ║                      /                        \                 ")
        print("    ║                     |                          |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |_____________|     |                ")
        print("    ║                      \____/|             |\___/                 ")
        print("    ║                            |      |      |                      ")
        print("    ║                            |      |      |                      ")
        print("    ║                            |      |      |                      ")
        print("    ║                            |      |      |                      ")
        print("    ║                            |      |      |                      ")
        print("    ║                            |      |      |                      ")
        print("    ║                            |      |      |                      ")
        print("    ║                            |      |      |                      ")
        print("    ║                            |      |      |                      ")
        print("    ║                            |      |      |                      ")
        print("    ║                            \______/\_____/                      ")
        print("    ║                      ╔═════════════════════════╗                ")
        print("    ║                      ║                         ║                ")
        print("    ║                      ║                         ║                ")
        print("    ║                      ║                         ║                ")
        print("    ║                      ║                         ║                ")
        print("════╩══════════════════════╩═════════════════════════╩════════════════")
        print("                                                                      ")
        print("                               _ _ _ _ _ _ _ _ _ _                    ")
        print("                                                                      ")
        print("                                CHOSE YOUR LETTER                     ")
        print("                                                                      ")
    def Hangman1wrong():
        print("                                                                      ")
        print("    ╔══════════════════════════════════╤══                            ")
        print("    ║                                  │                              ")
        print("    ║                                  │                              ")
        print("    ║                                  │                              ")
        print("    ║                                  │                              ")
        print("    ║                              _________                          ")
        print("    ║                            /           \                        ")
        print("    ║                           |     ○   ○   |                       ")
        print("    ║                           |             |                       ")
        print("    ║                           |             |                       ")
        print("    ║                            \    ────   /                        ")
        print("    ║                              ─────────                          ")
        print("    ║                       __________╟──╢__________                  ")
        print("    ║                      /                        \                 ")
        print("    ║                     |                          |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |_____________|     |                ")
        print("    ║                      \____/|             |\___/                 ")
        print("    ║                            |      |      |                      ")
        print("    ║                            |      |      |                      ")
        print("    ║                            |      |      |                      ")
        print("    ║                            |      |      |                      ")
        print("    ║                            |      |      |                      ")
        print("    ║                            |      |      |                      ")
        print("    ║                            |      |      |                      ")
        print("    ║                            |      |      |                      ")
        print("    ║                            |      |      |                      ")
        print("    ║                            |      |      |                      ")
        print("    ║                            \______/\_____/                      ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("════╩═════════════════════════════════════════════════════════════════")
    def Hangman2wrong():
        print("                                                                      ")
        print("    ╔══════════════════════════════════╤══                            ")
        print("    ║                                  │                              ")
        print("    ║                                  │                              ")
        print("    ║                                  │                              ")
        print("    ║                                  │                              ")
        print("    ║                              _________                          ")
        print("    ║                            /           \                        ")
        print("    ║                           |     ○   ○   |                       ")
        print("    ║                           |             |                       ")
        print("    ║                           |             |                       ")
        print("    ║                            \    ────   /                        ")
        print("    ║                              ─────────                          ")
        print("    ║                       __________╟──╢__________                  ")
        print("    ║                      /                        \                 ")
        print("    ║                     |                          |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |_____________|     |                ")
        print("    ║                      \____/|             |\___/                 ")
        print("    ║                                   |      |                      ")
        print("    ║                                   |      |                      ")
        print("    ║                                   |      |                      ")
        print("    ║                                   |      |                      ")
        print("    ║                                   |      |                      ")
        print("    ║                                   |      |                      ")
        print("    ║                                   |      |                      ")
        print("    ║                                   |      |                      ")
        print("    ║                                   |      |                      ")
        print("    ║                                   |      |                      ")
        print("    ║                                    \_____/                      ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("════╩═════════════════════════════════════════════════════════════════")
    def Hangman3wrong():
        print("                                                                      ")
        print("    ╔══════════════════════════════════╤══                            ")
        print("    ║                                  │                              ")
        print("    ║                                  │                              ")
        print("    ║                                  │                              ")
        print("    ║                                  │                              ")
        print("    ║                              _________                          ")
        print("    ║                            /           \                        ")
        print("    ║                           |     ○   ○   |                       ")
        print("    ║                           |             |                       ")
        print("    ║                           |             |                       ")
        print("    ║                            \    ────   /                        ")
        print("    ║                              ─────────                          ")
        print("    ║                       __________╟──╢__________                  ")
        print("    ║                      /                        \                 ")
        print("    ║                     |                          |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |             |     |                ")
        print("    ║                     |      |_____________|     |                ")
        print("    ║                      \____/|             |\___/                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("════╩═════════════════════════════════════════════════════════════════")
    def Hangman4wrong():
        print("                                                                      ")
        print("    ╔══════════════════════════════════╤══                            ")
        print("    ║                                  │                              ")
        print("    ║                                  │                              ")
        print("    ║                                  │                              ")
        print("    ║                                  │                              ")
        print("    ║                              _________                          ")
        print("    ║                            /           \                        ")
        print("    ║                           |     ○   ○   |                       ")
        print("    ║                           |             |                       ")
        print("    ║                           |             |                       ")
        print("    ║                            \    ────   /                        ")
        print("    ║                              ─────────                          ")
        print("    ║                       __________╟──╢__________                  ")
        print("    ║                      /                        \                ")
        print("    ║                     |                                           ")
        print("    ║                     |      |             |                      ")
        print("    ║                     |      |             |                      ")
        print("    ║                     |      |             |                      ")
        print("    ║                     |      |             |                      ")
        print("    ║                     |      |             |                      ")
        print("    ║                     |      |             |                      ")
        print("    ║                     |      |_____________|                      ")
        print("    ║                      \____/|                                    ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("════╩═════════════════════════════════════════════════════════════════")
    def Hangman5wrong():
        print("                                                                      ")
        print("    ╔══════════════════════════════════╤══                            ")
        print("    ║                                  │                              ")
        print("    ║                                  │                              ")
        print("    ║                                  │                              ")
        print("    ║                                  │                              ")
        print("    ║                              _________                          ")
        print("    ║                            /           \                        ")
        print("    ║                           |     ○   ○   |                       ")
        print("    ║                           |             |                       ")
        print("    ║                           |             |                       ")
        print("    ║                            \    ────   /                        ")
        print("    ║                              ─────────                          ")
        print("    ║                       __________╟──╢__________                  ")
        print("    ║                      /____               ____ \                 ")
        print("    ║                            |             |                      ")
        print("    ║                            |             |                      ")
        print("    ║                            |             |                      ")
        print("    ║                            |             |                      ")
        print("    ║                            |             |                      ")
        print("    ║                            |             |                      ")
        print("    ║                            |             |                      ")
        print("    ║                            |_____________|                      ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("════╩═════════════════════════════════════════════════════════════════")
    def Hangman6wrong():
        print("                                                                      ")
        print("    ╔══════════════════════════════════╤══                            ")
        print("    ║                                  │                              ")
        print("    ║                                  │                              ")
        print("    ║                                  │                              ")
        print("    ║                                  │                              ")
        print("    ║                              _________                          ")
        print("    ║                            /           \                        ")
        print("    ║                           |     ○   ○   |                       ")
        print("    ║                           |             |                       ")
        print("    ║                           |             |                       ")
        print("    ║                            \    ────   /                        ")
        print("    ║                              ─────────                          ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("════╩═════════════════════════════════════════════════════════════════")
    def Hangman7wrong():
        print("                                                                      ")
        print("    ╔══════════════════════════════════╤══                            ")
        print("    ║                                  │                              ")
        print("    ║                                  │                              ")
        print("    ║                                  │                              ")
        print("    ║                                  │                              ")
        print("    ║                              _________                          ")
        print("    ║                            /           \                        ")
        print("    ║                           |     X   X   |                       ")
        print("    ║                           |             |                       ")
        print("    ║                           |             |                       ")
        print("    ║                            \    ────   /                        ")
        print("    ║                              ─────────                          ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("    ║                                                                 ")
        print("════╩═════════════════════════════════════════════════════════════════")
        print("                                     YOU DIED                         ")

    def Animals():
        Animals = ["JACKRABBIT", "AMBERJACK", "CARJACK", "APPLEJACK", "BLACKSHAFT", "JACKSHAFT"]
        RandAnimal = random.choice(Animals)
        Numberofletters = len(RandAnimal)
        var = " _"
        PositiveFeedback = 0
        newvar = Numberofletters
        Guessesthatarewrong = 0
        while newvar > 0 and PositiveFeedback != Numberofletters:
            var = var + " _"
            newvar -= 1
        #add print thing
            Guess = input("                  ¿What is your guess?")
            if Guess in RandAnimal:
                print("                      Correct!")
                count = 0
                while count < Numberofletters:
                    if Guess == RandAnimal [count]:
                        print("YOUR LETTER IS IN POSITION" + str(count))
                        PositiveFeedback += 1
                    count +=1
            else:
                Guessesthatarewrong += 1
                print(Guessesthatarewrong)
                if(Guessesthatarewrong == 1):
                    Hangman1wrong()
                if(Guessesthatarewrong == 2):
                    Hangman2wrong()
                if(Guessesthatarewrong == 3):
                    Hangman3wrong()
                if(Guessesthatarewrong == 4):
                    Hangman4wrong()
                if(Guessesthatarewrong == 5):
                    Hangman5wrong()
                if(Guessesthatarewrong == 6):
                    Hangman6wrong()
                if(Guessesthatarewrong == 7):
                    Hangman7wrong()
                    break


            if PositiveFeedback == Numberofletters:
                print(RandAnimal)
                print("                  `•.,¸,.•*¯`•.,¸,.•....╭━━━━╮")
                print("                  `•.,¸,.•*¯`•.,¸,.•*¯.|::::::::/:__:/")
                print("                  `•.,¸,.•*¯`•.,¸,.•* <|::::::::(｡ ●ω●｡)")
                print("                  `•.,¸,.•*¯`•.,¸,.•* ╰し---し---Ｊ･ﾟ YOU WIN!")


    print("                                                                      ")
    print("                      ________________________                        ")
    print("                         WELCOME TO HANGMAN                           ")
    print("                      ~~~~~~~~~~~~~~~~~~~~~~~~                        ")
    print("                              David Han                               ")
    print("                                                                      ")
    print("                        ¡¡CHOSE YOUR MODE!!                           ")
    print("                      ¿Easy, Medium(Unavalible), or Hard(Unavalible)?                         ")
    Mode = input("                              ")

    if(Mode == "Easy"):
        print("                  ¡¡CHOOSE YOUR CATEGORY!!                            ")
        print("        ¿Animals, Foods(Unavalible), Colors(Unavalible), Logos(Unavalible), Occupations(Unavalible)?                  ")
        Category = input("                     ")



    if Category == "Animals":
        Animals()

def BinarytoOctal():
    Number = input("Please enter number  ")

    [num_bef_dec, num_aft_dec] = Number.split(".")
    output = ""
    if len(num_bef_dec) % 3 == 1:
        num_bef_dec = "00" + num_bef_dec
    if len(num_bef_dec) % 3 == 2:
        num_bef_dec = "0" + num_bef_dec

    for index in range(0, len(num_bef_dec), 3):
        cur_group = num_bef_dec[index: index+3]

        if cur_group == "000":
            output = output + "0"
        elif cur_group == "001":
            output = output + "1"
        elif cur_group == "010":
            output = output + "2"
        elif cur_group == "011":
            output = output + "3"
        elif cur_group == "100":
            output = output + "4"
        elif cur_group == "101":
            output = output + "5"
        elif cur_group == "110":
            output = output + "6"
        elif cur_group == "111":
            output = output + "7"

    output += "."

    if len(num_aft_dec) % 3 == 1:
        num_aft_dec = "00" + num_aft_dec
    if len(num_aft_dec) % 3 == 2:
        num_aft_dec = "0" + num_aft_dec

    for index in range(0, len(num_aft_dec), 3):
        cur_group = num_aft_dec[index: index+3]

        if cur_group == "000":
            output = output + "0"
        elif cur_group == "001":
            output = output + "1"
        elif cur_group == "010":
            output = output + "2"
        elif cur_group == "011":
            output = output + "3"
        elif cur_group == "100":
            output = output + "4"
        elif cur_group == "101":
            output = output + "5"
        elif cur_group == "110":
            output = output + "6"
        elif cur_group == "111":
            output = output + "7"
    print (output)

def OldMcdonald():
    def OldMacPig():
        print("Old MACDONALD had a farm E-I-E-I-O")
        print("And on his farm he had a pig E-I-E-I-O")
        print("With a oink oink here And a oink oink there")
        print("Here a oink, there a oink Everywhere a oink oink")
        print("Old MacDonald had a farm E-I-E-I-O")
    def OldMacCow():
        print("Old MACDONALD had a farm E-I-E-I-O")
        print("With a moo moo here And a moo moo there")
        print("And on his farm he had a cow E-I-E-I-O")
        print("Here a moo, there a moo Everywhere a moo moo")
        print("Old MacDonald had a farm E-I-E-I-O")

    if __name__ == '__main__':
        OldMacPig()
        print
        OldMacCow()

def Pattern1():
    Numberofreps = input("How many rows do you wish for?")
    Numberofreps = int(Numberofreps)
    Original = 0
    while Original <= Numberofreps:
        print(Original * "*" * 1)
        Original = Original + 1

def Pattern2():
    Numberofreps = input("How many rows do you wish for?")
    Numberofreps = int(Numberofreps)
    Star = "*"
    while Numberofreps > 0:
        Numberofreps = Numberofreps - 1
        print(Numberofreps * Star * 2)

if Mode == "BMI calculator":
    BMIcalculator()

if Mode == "Addition":
    n1 = input("what is your X input?")
    n2 = input("What is your y input?")
    print(Addition(int(n1), int(n2)))

if Mode == "Subtraction":
    n1 = input("What is your X input?")
    n2 = input("What is your y input?")
    print(Subtraction(int(n1), int(n2)))

if Mode == "Multiplication":
    n1 = input("What is your X value?")
    n2 = input("What is your Y value?")
    print(Multiplication(int(n1), int(n2)))

if Mode == "Division":
    n1 = input("What is your X value?")
    n2 = input("What is your Y value?")
    print(Division(int(n1), int(n2)))

if Mode == "Exponents":
    n1 = input("What is your X value?")
    n2 = input("What is your Y value?")
    print(Exponents(int(n1), int(n2)))

if Mode == "MinMax":
    print("Not really working Right now.")

if Mode == "Hangman":
    Hangman()

if Mode == "Binary to Octal":
    BinarytoOctal()

if Mode == "Binary to Decimal":
    Number = input("what is your binary number?? ")
    decimal = int(Number, 2)
    print (decimal)

if Mode == "Old Mcdonald":
    OldMcdonald()

if Mode == "Pattern":
    PatternID = input("What number pattern?")
    if PatternID == "1":
        Pattern1()
    if PatternID == "2":
        Pattern2()
