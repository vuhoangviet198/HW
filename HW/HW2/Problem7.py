def convert(a):
    b = a[0]
    for i in a[1:]:
        if i.isupper():
            b += " " + i.lower()
        else:
            b += i
    return b


def main():
    a = input("Enter unseparated string: ")
    print(convert(a))

main()