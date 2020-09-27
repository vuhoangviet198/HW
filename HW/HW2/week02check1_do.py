# Programming Morse Code

def main():
    # Dictionary of Morse codes.
    morseDict = {
        " ": " ",
        ",": "--..--",
        ".": ".-.-.-",
        "?":"-----",
        "0":".----",
        "1":"..---",
        "2":"...--",
       "3":"....-",
        "4":".....",
        "5":"-....",
        "6":"--...",
        "7":"---..",
        "8":"----.",
        "9":".-",
        "A":"-...",
        "B":"-.-.",
        "C":"-..",
        "D":".",
        "E":"..-.",
        "F":"--.",
        "G":"....",
        "H":"..",
        "I":".---",
        "J":"-.-",
        "K":".-..",
        "L":"--",
        "M":"-.",
        "N":"---",
        "O":".--.",
        "P":"--.-",
        "Q":"--.-",
        "R":".-.",
        "S":"...",
        "T":"-",
        "U":"..-",
        "V":"...-",
        "W":".--",
        "X":"-..-",
        "Y":"-.-",
        "Z":"--..",
    }

    #Ask user to input.
    n = input("please type in something: ")

    # Display the Morse code for this character.
    for i in n:
        print(morseDict.get(i.upper()), ',', sep='', end='')







# Call the main function.
main()
