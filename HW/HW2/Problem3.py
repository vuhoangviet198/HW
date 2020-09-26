def convert(a):
    if a == "A" or a == "B" or a == "C":
        return "2"
    elif a == "D" or a == "E" or a == "F":
        return "3"
    elif a == "G" or a == "H" or a == "I":
        return "4"
    elif a == "J" or a == "K" or a == "L":
        return "5"
    elif a == "M" or a == "N" or a == "O":
        return "6"
    elif a == "S":
        return "7"
    elif a == "T" or a == "U" or a == "V":
        return "8"
    elif a == "W" or a == "X" or a == "Y" or a == "Z":
        return "9"
    else:
        return a


def main():

   n = input("Enter telephone number(XXX-XXX-XXXX): ")
   for i in n:
      print(convert(i), end='')






main()