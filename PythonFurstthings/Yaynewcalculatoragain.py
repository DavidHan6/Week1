
a = input("What is your x value? ")
b = input("What is your y value? ")

float(a)
float(b)
Powers(a , b)

def Addition(a , b):
    return a + b

def Multiplication(a , b):
    result = 0
    for x in range (b):
        result= result + a
    return result

def Division(a , b):
    return a / b

def Subtraction(a , b):
    return a - b

def Powers(a , b):
    # 0 <= i <= (b-1)
    for i in range(b):
        if b > 0:
            b = b - 1
            answer = a * a
    print (answer)
