
def convert(a):
    sentence = a.split('. ')
    b= ""
    for i in sentence:
        b = b + ". " + i.capitalize()
    return b
    #. Hello. Hi
def main():
    #"hello. hi
    sentence = input("Enter a sentence: ")
    print(convert(sentence)[2::])
    #Hello. Hi

main()