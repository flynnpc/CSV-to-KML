import string
def alphabet():

    alphabet = string.ascii_letters
    alpha = alphabet[:26]
    alphaDict = {}

    num = 0
    x = 0
    while len(alphaDict) < 26:
        alphaDict[alpha[x]] = num
        num += 1
        x += 1
    return(alphaDict
