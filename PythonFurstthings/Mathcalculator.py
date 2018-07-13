#Ask Specific Operation
What(Jeff)

#Ask what Numbers to add
if Operation == "Addition":
    Que(Numbers)
    What(Numeros)
    Numeros+Numbers

if Operation == "Subtration":
    Que(Numbers)
    What(Numeros)
    Answer = Numbers - Numeros

if Operation == "Division":
    Que(Numbers)
    What(Numeros)
    Answer = Numbers / Numeros

if Operation == "Multiplication":



#What number you need

def Que(Numbers):
    Numbers = input("What is your first number??")
    return Numbers

def What(Numeros):
    Numeros = input("what is your second number??")
    return Numeros

def TheAnswer(Answer):
    print(Answer)

def What(Jeff):
    Operation = Input("What is your Operation??")

#JUNK that im working on
