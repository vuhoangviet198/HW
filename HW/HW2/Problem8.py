def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))


def convertPig(a):
    b = []
    b.append(a[1:] + a[0] + "ay")
    return b
def convertAllPig(a):
    b = list(a.split(" "))
    c = []
    for i in b:
        c = c + convertPig(i)
    return listToString(c)


def main():
    a = input("Enter in Latin: ")
    print(convertAllPig(a))
main()