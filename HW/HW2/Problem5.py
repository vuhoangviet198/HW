def vowelCounter(a):
    counter = 0
    list = ["a", "e", "u", "o", "i"]
    for i in a:
        if i in list:
            counter = counter + 1
    return counter
def consonantCounter(a):
    counter = 0
    list = ["b", "c", "d", "f", "g", "h",
            "j", "k", "l", "m", "n", "p",
            "q", "r", "s", "t", "v", "w",
            "x", "y", "z"]
    for i in a:
        if i in list:
            counter = counter + 1
    return counter



def main():
    n = input("Enter a String: ")
    print("Vowels: ", vowelCounter(n))
    print("Consonants: ", consonantCounter(n))
main()