from collections import Counter

def main():

    string = 'vu hoang viet'
    #print(Counter(list(string)))
    print((Counter(list(string)).most_common(1))[0][0])
main()