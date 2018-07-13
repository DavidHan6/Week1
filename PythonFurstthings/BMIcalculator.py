#bmi calculator to see if ur fat.
print("HELLO. WELCOME TO THE AUTOMATED BMI CALCULATOR TO SEE IF YOUR FAT")
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
