



def lineFormatted(line): #used for fucntion => timeOccured_Calculator(word) & sumScore_Calculator(word)
    #get rid of enter
    line.rstrip("\n")

    #get rid of, except for letter, number, space
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890')
    line = ''.join(filter(whitelist.__contains__, line))


    #lowercase all
    for character in line:
        if character.isupper():
            line = line.replace(character,character.lower())
    return line

def timeOccured_Calculator(word, file):
    timeOccured = 0
    lines = file.readlines()
    for line in lines:
        line = lineFormatted(line)
        if word in line:
            timeOccured = timeOccured + 1
    return timeOccured

def lineScore(line):
    #get rid of enter
    line.rstrip("\n")

    #get rid of, except for letter, number, space
    whitelist = set('1234567890')
    line = ''.join(filter(whitelist.__contains__, line))


    #lowercase all
    for character in line:
        if character.isupper():
            line = line.replace(character,character.lower())
    score = line
    return score

def sumScore_Calculator(word, file):
    sumScore = 0
    lines = file.readlines()
    for line in lines:
        line = lineFormatted(line)

        if word in line:
            score = lineScore(line)
            sumScore = sumScore + int(score)


    return sumScore


#main function
def main():
    # fileName = input("Learning data file name: ")
    # file = open(fileName, "r")
    # print(fileName)
    # word = input("Get score of the word: ")
    # # ws = dict {word : score}
    # # ws = {
    # #     "oh": 2,
    # #     "nice": 4
    # # }
    # sumScore = sumScore_Calculator(word, file)
    # timeOccured = timeOccured_Calculator(word, file)
    #
    #
    #
    # # scoreOfWord = sumScore/timeOccured
    #
    # #add {word:score} to word-score dictionary(ws)
    # # ws[word] = scoreOfWord
    # # print(ws)
    # print(timeOccured)

    fileName = input("Learning data file name: ")
    word = input("Get score of a word: ")

    file = open(fileName, "r")

    timeOccured = timeOccured_Calculator(word, file)

    file = open(fileName, "r")
    sumScore = sumScore_Calculator(word, file)

    scoreOfWord = sumScore / timeOccured

    print(scoreOfWord)

    #  ws = dict {word : score}
    ws = {}
    # add {word:score} to word-score dictionary(ws)
    ws[word] = scoreOfWord
    print(ws)
main()

