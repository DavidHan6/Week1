def BinaryToOctal(number):
    [num_bef_dec, num_aft_dec] = number.split(".")
    output = ""

    count = 0
    slide_a = len(num_bef_dec)
    while count < side_a:
        cur_group = num_bef_dec[side_a-1-3*(count-1): side_a-1-3*count]

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
            output = output + "8"
        elif cur_group == "111":
            output = output + "7"
print(output)


def Converting2():
    if Number >= 1000000000:
        Number = Number - 1000000000
        Answer = Answer + 512
        if Number >= 100000000:
            Number = Number - 100000000
            Answer = Answer + 256
            if Number >= 10000000:
                Number = Number - 10000000
                Answer = Answer + 128
                if Number = Number >= 1000000:
                    Number = Number - 1000000
                    Answer = Answer + 64
                    if 0:
                        pass



#Hangman was Here...

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








#NYAN CAT COZ WHY NOT


        `•.,¸,.•*¯`•.,¸,.•....╭━━━━╮
        `•.,¸,.•*¯`•.,¸,.•*¯.|::::::::/:__:/
        `•.,¸,.•*¯`•.,¸,.•* <|::::::::(｡ ●ω●｡)
        `•.,¸,.•*¯`•.,¸,.•* ╰し---し---Ｊ･ﾟ I am a unicorn!


#Hangman code with 2 indentations

else:
    print("                        UR BAD U GOT IT WRONG CHANGE LATER PLS")
    Guessesthatarewrong += 1
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
    if(Guessesthatarewrongt == 6):
        Hangman6wrong()
    if(Guessesthatarewrong == 7):
        print("Died u")
        break
