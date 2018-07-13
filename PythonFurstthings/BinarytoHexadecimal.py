Number = input("Please enter number  ")

[num_bef_dec, num_aft_dec] = Number.split(".")
output = ""
if len(num_bef_dec) % 4 == 3:
    num_bef_dec = "000" + num_bef_dec
if len(num_bef_dec) % 4 == 1:
    num_bef_dec = "00" + num_bef_dec
if len(num_bef_dec) % 4 == 2:
    num_bef_dec = "0" + num_bef_dec

for index in range(0, len(num_bef_dec), 3):
    cur_group = num_bef_dec[index: index+3]

    if cur_group == "0000":
        output = output + "0"
    elif cur_group == "0001":
        output = output + "1"
    elif cur_group == "0010":
        output = output + "2"
    elif cur_group == "0011":
        output = output + "3"
    elif cur_group == "0100":
        output = output + "4"
    elif cur_group == "0011":
        output = output + "5"
    elif cur_group == "0110":
        output = output + "6"
    elif cur_group == "0111":
        output = output + "7"
    elif cur_group == "1000":
        output = output + "8"
    elif cur_group == "1001":
        output = output + "9"
    elif cur_group == "1010":
        output = output + "10"
    elif cur_group == "1011":
        output = output + "11"
    elif cur_group == "1100":
        output = output + "12"
    elif cur_group == "1101":
        output = output + "13"
    elif cur_group == "1110":
        output = output + "14"
    elif cur_group == "1111":
        output = output + "15"

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
