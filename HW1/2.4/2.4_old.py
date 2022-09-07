import base64
import sys

englishFreq = {32: 0.167564443682168,    101: 0.08610229517681191,    116: 0.0632964962389326,    97: 0.0612553996079051,    110: 0.05503703643138501,    105: 0.05480626188138746,    111: 0.0541904405334676,    115: 0.0518864979648296,    114: 0.051525029341199825,    108: 0.03218192615049607,    100: 0.03188948073064199,    104: 0.02619237267611581,    99: 0.02500268898936656,    10: 0.019578060965172565,    117: 0.019247776378510318,    109: 0.018140172626462205,    112: 0.017362092874808832,    102: 0.015750347191785568,    103: 0.012804659959943725,    46: 0.011055184780313847,    121: 0.010893686962847832,    98: 0.01034644514338097,    119: 0.009565830104169261,    44: 0.008634492219614468,    118: 0.007819143740853554,    48: 0.005918945715880591,    107: 0.004945712204424292,    49: 0.004937789430804492,    83: 0.0030896915651553373,    84: 0.0030701064687671904,    67: 0.002987392712176473,    50: 0.002756237869045172,    56: 0.002552781042488694,    53: 0.0025269211093936652,    65: 0.0024774830020061096,    57: 0.002442242504945237,    120: 0.0023064144740073764,    51: 0.0021865587546870337,    73: 0.0020910417959267183,    45: 0.002076717421222119,    54: 0.0019199098857390264,    52: 0.0018385271551164353,    55: 0.0018243295447897528,    77: 0.0018134911904778657,    66: 0.0017387002075069484,    34: 0.0015754276887500987,    39: 0.0015078622753204398,    80: 0.00138908405321239,
               69: 0.0012938206232079082,    78: 0.0012758834637326799,    70: 0.001220297284016159,    82: 0.0011037374385216535,    68: 0.0010927723198318497,    85: 0.0010426370083657518,    113: 0.00100853739070613,    76: 0.0010044809306127922,    71: 0.0009310209736100016,    74: 0.0008814561018445294,    72: 0.0008752446473266058,    79: 0.0008210528757671701,    87: 0.0008048270353938186,    106: 0.000617596049210692,    122: 0.0005762708620098124,    47: 0.000519607185080999,    60: 0.00044107665296153596,    62: 0.0004404428310719519,    75: 0.0003808001912620934,    41: 0.0003314254660634964,    40: 0.0003307916441739124,    86: 0.0002556203680692448,    89: 0.00025194420110965734,    58: 0.00012036277683200988,    81: 0.00010001709417636208,    90: 0.00008619977698342993,    88: 0.00006572732994986532,    59: 0.00000741571610813331,    63: 0.000004626899793963519,    127: 0.0000031057272589618137,    94: 0.0000022183766135441526,    38: 0.0000020282300466689395,    43: 0.0000015211725350017046,    91: 6.97204078542448e-7,    93: 6.338218895840436e-7,    36: 5.070575116672349e-7,    33: 5.070575116672349e-7,    42: 4.436753227088305e-7,    61: 2.5352875583361743e-7,    126: 1.9014656687521307e-7,    95: 1.2676437791680872e-7,    9: 1.2676437791680872e-7,    123: 6.338218895840436e-8,    64: 6.338218895840436e-8,    5: 6.338218895840436e-8,    27: 6.338218895840436e-8,    30: 6.338218895840436e-8}

englishLetterFrequencies = [[b'E'[0], 0.13], [b'T'[0], 0.091], [b'A'[0], 0.082], [b'O'[0], 0.075], [b'I'[0], 0.07], [b'N'[0], 0.067], [b'S'[0], 0.063], [b'H'[0], 0.061], [b'R'[0], 0.06], [b'D'[0], 0.043], [b'L'[0], 0.04], [b'C'[0], 0.028], [b'U'[
    0], 0.028], [b'M'[0], 0.024], [b'W'[0], 0.024], [b'F'[0], 0.022], [b'G'[0], 0.02], [b'Y'[0], 0.02], [b'P'[0], 0.019], [b'B'[0], 0.015], [b'V'[0], 0.0098], [b'K'[0], 0.0077], [b'J'[0], 0.0015], [b'X'[0], 0.0015], [b'Q'[0], 0.00095], [b'Z'[0], 0.00074]]

englishLetterFrequenciesDict = {e[0]: e[1] for e in englishLetterFrequencies}


def findInList(list, matcher):
    for i, e in enumerate(list):
        if matcher(e):
            return i

    return -1


def encode(text):
    return base64.b64encode(text)


def decode(text):
    return base64.b64decode(text)


def encrypt(cleartext, key):
    to_return = bytearray(len(cleartext))
    for i in range(len(cleartext)):
        to_return[i] = cleartext[i] ^ key[i % len(key)]
    return bytes(to_return)


def encryptWithSingleSymbolKey(c, k):
    to_return = bytearray(len(c))
    for i in range(len(c)):
        to_return[i] = c[i] ^ k
    return bytes(to_return)


encrypted = decode("cDkSNzYiOBliNTk7G2IhMSIEJ2IxdxQnMCQ2HixiND4ENjciNRYsITV3ACorMz9XJzQ1OQM3Izw7DmImOTIEYiMnNg5sYhkxW2IqPyASNCcie1c2KjV3BCs4NXcYJGIkPxJiMjk7EmIrI3cENyQ2PhQrJz4jGztiOTkUMCcxJBImbnAjHydiND4ENjciNRYsITV3FCM3IzITYiApdwQ3ITh3FixiOTkULS85ORBiLDUiAzAtPncAKy48dwEnMCl3GyspNTsOYiU/dxgsYjE5E2ItPnceLCEiMhYxKz4wVzcsJD4bYjY4Mlc1Kj87EmIyOTsSYisjdxMnMSQlGDsnNHlXCzFwIx8nMDV3FmIhPyUFJzEgOBkmKz4wVzIqNTkYLyc+OBliJD8lVy8rPjMEbmIxORNiKyN3AyonIjJXLSw1dxEtMHA6FiEqOTkSMX1wAx8nMDV3Ey0nI3cEJyc9dwMtYjIyVy0sNXcRLTBwIx8nYjgiGiMscDoeLCZ+dyMqJ3A6FigtIj4DO2I/MVc2KjU6VzEnNTpXNi1wNRJiYCMiFWIhIj4DKyExO1tgYjl5EmxiJDhXIS0iJRIxMj85E2IrPncDKisjdxYsIzw4EDtiJDhXMis8MgRiLTZ3BDcgfTQFKzY5NBYuYiM+DSdscBYZYis0MhZiMiIyBCcsJDITYjY/dwQ3ITh3FmIvOTkTYjU5OxtiLT53FjQnIjYQJ2I3PgEnYiI+BCdiJDhXLicjJFc2KjE5Vy0sNXceJicxdx4sYiIyBy47fnc2YjE9NhsuKyM/VzIwPycYMDY5OBliIyIyVzE3IDIFITA5Ix4hIzx5VwMscD4TJyNwJwUnMTU5AycmcCMYYjElNB9iI3A6HiwmcDoWO2I3PgEnYiI+BCdiJDhXI2InPxguJ3B1AyonPyUOYGIzOBkxKyMjHiwlcDgRYjE1NBgsJjElDm5iJDIFNisxJQ5iIz4zVy8tIjJXMCc9OAMnYjkzEiMxfnc2LCs9NhsxoNDOVy8rPjMEYjE1MhpiNj93FSdiJjIFO2I0MhErLDkjEi47cCQCIG8zJR42KzM2G2xiETMfJzA5ORBiNj93AyorI3cWLCM8OBA7YicyVyMxO3tXYAExOVcjYj02FCorPjJXICdwOhYmJ3AjGGIgNXcENzI1JVohMDkjHiEjPGh9Fio1dwctMiU7FjBiJj4SNWIkPxY2YiM0HicsJD4ENjFwJwUtITUyE2IrPjIPLTAxNRs7YjYlGC9iJzIbLm81JAMjIDw+BConNHcRIyEkdwMtYicyGy5vNSQDIyA8PgQqJzR3ESMhJHtXLCcmMgViIDU+GSViOTkRLjc1ORQnJnA1DmIjPi5XNywgJRg0JzR3FC0sOjIUNjciMltiKyN3BjcrJDJXLysjIxYpJz55VxIwPyEeJic0dx42YjkkVy8jNDJXIS41NgViNTg+FCpiMSUSYjIiOAEnJnAxFiE2I3cWLCZwIB8rITh3FjAncDQYLCg1NAM3MDUkW2IsP3cfIzA9dxQjLHAlEjE3PCNZYgE/OR0nISQiBScxcDYFJ2I/MVclMDU2A2IrPScYMDYxORQnYiM+GSEncCMfJztwJAIlJTUkA2I3IzIRNy5wOx4sJyN3GCRiIjIEJyMiNB9sSAQ/EmIrIzgbIzY1M1cvIz53Ey0nI3cZLTZwMxI0Jzw4B2IjPi5XKywkMhsuJzMjAiMucCcYNScieVcLNnA+BGIsNTQSMTExJQ5iJD8lVyorPXcDLWIyMlcrLz0yBTEnNHceLGIxOVcnLCY+BS0sPTIZNmI/MVctNjgyBWIvNTlbYjU4OAQnYiQyFCosOSYCJzFwPxJiIzIkGDAgI3cTNzA5ORBiNjgyVyQrIiQDYjYnMhk2O3AuEiMwI3cYJGI4PgRiLjkxEmxiGDJXLyMpdwMqJz53BycwODYHMWI0OFcjYjw+AzYuNXcFJzE1NgUhKnA4EWIqOSRXLTU+dxYsJnA6FikncDZXNCciLlckJyd3EysxMzgBJzA5MgRiNTg+FCpiMSUSYjIxJAQnJnA4GWI2P3cYNio1JVcvJz55VwQwPzpXNio5JFcyLTk5A2ItNncBKycndwMqJ3AkEiMwMz9XJC0idxknNXAjEiEqPj4GNycjdxo3MSR3FSdiIjIQIzA0MhNiIyN3FCMwIj4SJmI/IgNiICl3AyoncD8CLyM+dxQtLz0iGSs2KXcWMWIxdwAqLTwyW2IwMSMfJzBwIx8jLHA1DmIrPjMeNCs0IhYuMX5dNjAncC4YN2IgNg4rLDd3FjY2NTkDKy0+aFcFLT8zWWILNncOLTdwNgUnYj44A2IuOSQDJyw5ORBiITElEiQ3PDsObmIpOAJiNTk7G2IvOSQEYjY4PhklMX53Pi8yPyUDIywkdwMqKz4wBGxiGXcAKy48dxktNnAnFjcxNXtXC2InPhsuYj44A2IwNScSIzZwOg4xJzwxW2IjPjNXOy0ldwArLjx3GS02cD4ZNiciJQIyNnA6EmxiCTgCYjY4PhkpYiQ/FjZiMjIUIzcjMlc7LSVwBSdiIz4DNis+MFc1KjUlEmI7PyJXIzA1e1cjLDR3PmIjPXcEKzYkPhklYic/EjAncB5XIy98dwMqIyR3Di03cDYFJ2I5OVchLT4jBS0ucDgRYjU4Ng==")


def frequencyAnalysis(text):
    scores = [0 for i in range(256)]

    for guess in range(256):
        text = encryptWithSingleSymbolKey(text, guess)
        counts = dict.fromkeys(range(256), 0)
        letterCounts = {}
        for e in text:
            counts[e] += 1

        score = 0
        for key in englishFreq:
            score += englishFreq[key] * counts[key]/len(text)

        # for key in counts:
        #     if key >= b'a'[0] and key <= b'z'[0]:
        #         counts[key-32] += counts[key]

        # for key in counts:
        #     if key >= b'A'[0] and key <= b'Z'[0] and counts[key] > 0:
        #         letterCounts[key] = counts[key]

        # if (len(letterCounts) < 5):
        #     scores[guess] = float(0)
        #     continue

        # for key in letterCounts:
        #     letterCounts[key] /= len(text)

        # score = 0

        # for i in range(b'A'[0], b'Z'[0]+1):
        #     if i in letterCounts:
        #         score += letterCounts[i]*englishLetterFrequenciesDict[i]

        scores[guess] = score

        # letterCounts = [[k, v] for [k, v] in letterCounts.items()]

        # letterCounts = sorted(letterCounts, key=lambda e: e[1], reverse=True)

        # score = 0

        # for englishLetterIndex, [letter, value] in enumerate(englishLetterFrequencies):
        #     letterCountIndex = findInList(
        #         letterCounts, lambda x: x[0] == letter)
        #     if letterCountIndex == -1:
        #         score += 1
        #     else:
        #         avgScores.append(
        #             abs(englishLetterIndex-letterCountIndex)**2 * value**2)
        #         score += abs(englishLetterIndex-letterCountIndex) * value

        # scores[guess] = score

    scores = [[i, e] for i, e in enumerate(scores)]

    scores = sorted(scores, key=lambda e: e[1], reverse=True)
    # scores = [e[0] for e in scores]

    # print(scores)
    # sys.exit()

    # return avg([e[1] for e in scores[:2]])
    print((scores[0][1]-scores[1][1])/scores[0][1])
    return scores[0]


def avg(arr):
    return sum(arr)/len(arr)


def crack(decodedText):
    scoresForKeyLength = [0 for e in range(2, 10)]
    for keyLength in range(2, 10):
        print()
        splitText = [[e for i, e in enumerate(
            decodedText) if i % keyLength == offset] for offset in range(keyLength)]

        scores = [frequencyAnalysis(e) for e in splitText]
        scoresForKeyLength[keyLength-2] = scores

    scoresForKeyLength = sorted(
        scoresForKeyLength,
        key=lambda s: avg([e[1] for e in s]),
        reverse=True
    )

    keyGuess = [a[0] for a in scoresForKeyLength[0]]

    print(keyGuess)
    print(encrypt(encrypted, keyGuess))
    # print(scores)

    # scores = [[i, frequencyAnalysis(encrypt(decodedText, i))]
    #           for i in range(256)]

    # scores = [e for e in scores if e[1] < float('inf')]

    # scores = sorted(scores, key=lambda e: e[1])

    # for e in scores[:3]:
    #     print('Decryption with key {}:'.format(hex(e[0])))
    #     print(encrypt(decodedText, e[0]))


crack(encrypted)
