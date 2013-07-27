import re

digitWords = {"0": "", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
tensDigitWords = {"0": "", "2": "twenty", "3": "thirty", "4": "forty", "5": "fifty", "6": "sixty", "7": "seventy", "8": "eighty", "9": "ninety"}
teensDigitWords = {"10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen", "15": "fifteen", "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen"}

def numberToWords(x):
    strX = str(x)
    numberString = ""
    if len(strX) == 3:
        numberString += digitWords[strX[0]] + " hundred"
        strX = strX[1:]

    if len(strX) == 2:
        if int(strX[0]) == 1:
            if numberString:
                numberString += " and "
            numberString += teensDigitWords[strX]
        elif int(strX[0]) != 0:
            if numberString:
                numberString += " and "
            numberString += tensDigitWords[strX[0]]
            if strX[1] != 0:
                numberString += " " + digitWords[strX[1]]
        elif int(strX[1]) != 0:
            if numberString:
                numberString += " and "
            numberString += digitWords[strX[1]]
    else:
        numberString = digitWords[strX]

    return numberString

total = 0
for x in xrange(1, 1000):
    numberString = numberToWords(x)
    numberString = re.sub(" ", "", numberString)
    total += len(numberString)

print total