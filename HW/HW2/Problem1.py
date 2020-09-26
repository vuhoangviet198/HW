def main():
    n = input("Enter a name: ")
    listN = list(n.split(" "))
    for word in listN:

        print(word[0].upper(),'.', sep='', end='')

main()