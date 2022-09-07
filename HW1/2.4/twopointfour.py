import base64
from gibberishclassifier import classify
import json

# englishFreq = {b' '[0]: 1293934, b'('[0]: 628, b','[0]: 83174, b'0'[0]: 299, b'4'[0]: 93, b'8'[0]: 40, b'<'[0]: 468, b'@'[0]: 8, b'D'[0]: 15683, b'H'[0]: 18462, b'L'[0]: 23858, b'P'[0]: 11939, b'T'[0]: 39800, b'X'[0]: 606, b'`'[0]: 1, b'd'[0]: 133779, b'h'[0]: 218406, b'l'[0]: 146161, b'p'[0]: 46525, b't'[0]: 289975, b'x'[0]: 4688, b'|'[0]: 33, b'#'[0]: 1, b"'"[0]: 31069, b'/'[0]: 5, b'3'[0]: 330, b'7'[0]: 41, b';'[0]: 17199, b'?'[0]: 10476, b'C'[0]: 21497, b'G'[0]: 11164, b'K'[0]: 6196, b'O'[0]: 33209, b'S'[0]: 34011, b'W'[0]: 16496, b'['[0]: 2085, b'_'[0]: 71, b'c'[0]: 66688, b'g'[0]: 57035, b'k'[0]: 29212, b'o'[0]: 281391, b's'[0]: 214978, b'w'[0]: 72894, b'\n'[0]: 124456, b'"'[0]: 470, b'&'[
#     0]: 21, b'*'[0]: 63, b'.'[0]: 78025, b'2'[0]: 366, b'6'[0]: 63, b':'[0]: 1827, b'>'[0]: 441, b'B'[0]: 15413, b'F'[0]: 11713, b'J'[0]: 2067, b'N'[0]: 27338, b'R'[0]: 28970, b'V'[0]: 3580, b'Z'[0]: 532, b'b'[0]: 46543, b'f'[0]: 68803, b'j'[0]: 2712, b'n'[0]: 215924, b'r'[0]: 208894, b'v'[0]: 33989, b'z'[0]: 1099, b'~'[0]: 1, b'!'[0]: 8844, b'%'[0]: 1, b')'[0]: 629, b'-'[0]: 8074, b'1'[0]: 928, b'5'[0]: 82, b'9'[0]: 948, b'='[0]: 1, b'A'[0]: 44486, b'E'[0]: 42583, b'I'[0]: 55806, b'M'[0]: 15872, b'Q'[0]: 1178, b'U'[0]: 14129, b'Y'[0]: 9099, b']'[0]: 2077, b'a'[0]: 244664, b'e'[0]: 404621, b'i'[0]: 198184, b'm'[0]: 95580, b'q'[0]: 2404, b'u'[0]: 114818, b'y'[0]: 85271, b'}'[0]: 2}


# englishFreq = {k: v/sum(englishFreq.values()) for k, v in englishFreq.items()}

englishFreq = {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0004419983201812568, 10: 0.034281134569915564, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0, 25: 0.0, 26: 0.0, 27: 0.0, 28: 0.0, 29: 0.0, 30: 0.0, 31: 0.0, 32: 0.1576243678401572, 33: 0.0011367011128939877, 34: 0.0006871985767504006, 35: 0.0, 36: 0.0, 37: 0.0, 38: 3.752107981165168e-07, 39: 0.0039749831952463795, 40: 8.461003497527455e-05, 41: 8.461003497527455e-05, 42: 0.0, 43: 0.0, 44: 0.017689688288001302, 45: 0.0024636341004330496, 46: 0.011893994694894525, 47: 4.164839859093337e-05, 48: 2.2137437088874492e-05, 49: 8.235877018657545e-05, 50: 6.509907347321567e-05, 51: 4.8777403755147186e-05, 52: 3.526981502295258e-05, 53: 3.208052323896219e-05, 54: 1.2757167135961572e-05, 55: 9.567875351971179e-06, 56: 6.941399765155562e-06, 57: 1.4070404929369382e-05, 58: 0.00022700253286049267, 59: 0.00108904934153319, 60: 3.752107981165168e-07, 61: 0.0013760856020923254, 62: 3.752107981165168e-07, 63: 0.002171157283301225, 64: 0.0, 65: 0.00792388924002366, 66: 0.002546180476018683, 67: 0.0031352614290616147, 68: 0.0023771480114671926, 69: 0.005772993339820728, 70: 0.002109247501611999, 71: 0.0018936888980940604, 72: 0.003474639595958004, 73: 0.009082915395405582, 74: 0.00039190767863270183, 75: 0.0009571627459952345, 76: 0.0039001286410221343, 77: 0.002754610074372408, 78: 0.00421080318186261, 79: 0.004887871067063865, 80: 0.0019711699279051213, 81: 0.00022456366267273531, 82: 0.004165402675290511, 83: 0.0055028415651768355, 84: 0.00727121005669998, 85: 0.0021332609926914565, 86: 0.0004480016929511211, 87: 0.0031170637053529637, 88: 5.215430093819584e-05, 89: 0.0013888427692282871, 90: 8.873735375455623e-05, 91: 0.001843973467343622, 92: 0.0, 93: 0.001843973467343622, 94: 0.0, 95: 0.0, 96: 0.0, 97: 0.050515004961224776, 98: 0.009541235385304906, 99: 0.013803254841110422,
               100: 0.027608573341610484, 101: 0.08584804300365999, 102: 0.013973225332657203, 103: 0.011869043176819777, 104: 0.04489359678384312, 105: 0.04153827422168617, 106: 0.0005616905647804257, 107: 0.006156458775495808, 108: 0.03005551056152735, 109: 0.019328796659573308, 110: 0.04429738682563598, 111: 0.057569718387411525, 112: 0.009598830242815793, 113: 0.0005249199065650071, 114: 0.043284317670721384, 115: 0.04525680083641991, 116: 0.05920038451602591, 117: 0.022965339714918587, 118: 0.006986237455530485, 119: 0.01489455544743231, 120: 0.000967668648342497, 121: 0.01744411282063404, 122: 0.00024932757534842546, 123: 0.0, 124: 0.0, 125: 0.0, 126: 0.0, 127: 0.0, 128: 0.0, 129: 0.0, 130: 0.0, 131: 0.0, 132: 0.0, 133: 0.0, 134: 0.0, 135: 0.0, 136: 0.0, 137: 0.0, 138: 0.0, 139: 0.0, 140: 0.0, 141: 0.0, 142: 0.0, 143: 0.0, 144: 0.0, 145: 0.0, 146: 0.0, 147: 0.0, 148: 0.0, 149: 0.0, 150: 0.0, 151: 0.0, 152: 0.0, 153: 0.0, 154: 0.0, 155: 0.0, 156: 0.0, 157: 0.0, 158: 0.0, 159: 0.0, 160: 0.0, 161: 0.0, 162: 0.0, 163: 0.0, 164: 0.0, 165: 0.0, 166: 0.0, 167: 0.0, 168: 0.0, 169: 0.0, 170: 0.0, 171: 0.0, 172: 0.0, 173: 0.0, 174: 0.0, 175: 0.0, 176: 0.0, 177: 0.0, 178: 0.0, 179: 0.0, 180: 0.0, 181: 0.0, 182: 0.0, 183: 0.0, 184: 0.0, 185: 0.0, 186: 0.0, 187: 0.0, 188: 0.0, 189: 0.0, 190: 0.0, 191: 0.0, 192: 0.0, 193: 0.0, 194: 0.0, 195: 0.0, 196: 0.0, 197: 0.0, 198: 0.0, 199: 0.0, 200: 0.0, 201: 0.0, 202: 0.0, 203: 0.0, 204: 0.0, 205: 0.0, 206: 0.0, 207: 0.0, 208: 0.0, 209: 0.0, 210: 0.0, 211: 0.0, 212: 0.0, 213: 0.0, 214: 0.0, 215: 0.0, 216: 0.0, 217: 0.0, 218: 0.0, 219: 0.0, 220: 0.0, 221: 0.0, 222: 0.0, 223: 0.0, 224: 0.0, 225: 0.0, 226: 0.0, 227: 0.0, 228: 0.0, 229: 0.0, 230: 0.0, 231: 0.0, 232: 0.0, 233: 0.0, 234: 0.0, 235: 0.0, 236: 0.0, 237: 0.0, 238: 0.0, 239: 0.0, 240: 0.0, 241: 0.0, 242: 0.0, 243: 0.0, 244: 0.0, 245: 0.0, 246: 0.0, 247: 0.0, 248: 0.0, 249: 0.0, 250: 0.0, 251: 0.0, 252: 0.0, 253: 0.0, 254: 0.0, 255: 0.0}


def singleLetterFreq(text):
    counts = dict.fromkeys(range(256), 0)
    for e in text:
        counts[e] += 1
    counts = {k: v/len(text) for k, v in counts.items()}
    return counts


def replaceEveryNth(text, n, offset, replace):
    return ''.join(replace if i % n == offset else chr(e) for i, e in enumerate(text))


def encode(text):
    return base64.b64encode(text)


def decode(text):
    return base64.b64decode(text)


def encrypt(cleartext, key):
    to_return = bytearray(len(cleartext))
    for i in range(len(cleartext)):
        to_return[i] = cleartext[i] ^ key[i % len(key)]
    return bytes(to_return)


encrypted = decode("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")
# encrypted = encrypt(
#     b"""HERMIASo will I grow, so live, so die, my lord,Ere I will yield my virgin patent upUnto his Lordship whose unwished yokeMy soul consents not to give sovereignty.THESEUSTake time to pause, and by the next new moon(The sealing day betwixt my love and meFor everlasting bond of fellowship),Upon that day either prepare to dieFor disobedience to your father's will,Or else to wed Demetrius, as he would,Or on Diana's altar to protestFor aye austerity and single life.DEMETRIUSRelent, sweet Hermia, and, Lysander, yieldThy crazed title to my certain right.LYSANDERYou have her father's love, Demetrius.Let me have Hermia's. Do you marry him.EGEUSScornful Lysander, true, he hath my love;And what is mine my love shall render him.And she is mine, and all my right of herI do estate unto Demetrius.LYSANDER, [to Theseus]I am, my lord, as well derived as he,As well possessed. My love is more than his;My fortunes every way as fairly ranked(If not with vantage) as Demetrius';And (which is more than all these boasts can be)I am beloved of beauteous Hermia.Why should not I then prosecute my right?Demetrius, I'll avouch it to his head,Made love to Nedar's daughter, Helena,And won her soul; and she, sweet lady, dotes,Devoutly dotes, dotes in idolatry,Upon this spotted and inconstant man.THESEUSI must confess that I have heard so much,And with Demetrius thought to have spoke thereof;But, being overfull of self-affairs,My mind did lose it.--But, Demetrius, come,And come, Egeus; you shall go with me.I have some private schooling for you both.--For you, fair Hermia, look you arm yourselfTo fit your fancies to your father's will,Or else the law of Athens yields you up(Which by no means we may extenuate)To death or to a vow of single life.--Come, my Hippolyta. What cheer, my love?--Demetrius and Egeus, go along.I must employ you in some businessAgainst our nuptial and confer with youOf something nearly that concerns yourselves.EGEUSWith duty and desire we follow you.[All but Hermia and Lysander exit.]LYSANDERHow now, my love? Why is your cheek so pale?How chance the roses there do fade so fast?""", b'PVvBD')


def ioc(text):
    counts = dict.fromkeys(range(256), 0)
    for e in text:
        counts[e] += 1

    return sum([
        e * (e - 1) /
        (
            (len(text) * (len(text) - 1))
            / len(counts.keys())
        )
        for e in counts.values()
    ])


def frequencyAnalysis(text):
    scores = list(range(256))

    for guess in scores:
        text = encrypt(text, [guess])
        textFreq = singleLetterFreq(text)

        score = 0
        for key in englishFreq:
            score += englishFreq[key] * textFreq[key]

        scores[guess] = score

    scores = [[i, e] for i, e in enumerate(scores)]
    scores = scores[32:]

    scores = sorted(scores, key=lambda e: e[1], reverse=True)
    return scores[0], scores


def avg(arr):
    return sum(arr)/len(arr)


def splitText(text, l):
    return [[e for i, e in enumerate(text) if i % l == offset] for offset in range(l)]


def printInColumns(text, l):
    ret = ''
    while (len(text) > 0):
        ret += text[:l]
        ret += '\n'
        text = text[l:]
    print(ret)


def crack(decodedText):
    scoresForKeyLength = [
        [
            frequencyAnalysis(e)[0]
            for e in splitText(decodedText, keyLength)
        ] for keyLength in range(5, 6)
    ]

    for score in scoresForKeyLength:
        keyGuess = [a[0] for a in score]

        print(''.join([chr(e) for e in keyGuess]))
        print(encrypt(encrypted, keyGuess))


# crack(encrypted)

def crack2(decodedText):
    scoresForKeyLength = [
        [
            frequencyAnalysis(e)[1]
            for e in splitText(decodedText, keyLength)
        ] for keyLength in range(5, 6)
    ]

    for score in scoresForKeyLength:

        keyGuess = [a[0][0] for a in score]

        # print(''.join([chr(e) for e in keyGuess]))
        # for j in range(len(keyGuess)):
        #     print(replaceEveryNth(encrypt(encrypted, keyGuess), 5, j, ' '))

        # print()
        # print()

        # print(encrypt(encrypted, keyGuess))
        n = 3
        for i0 in range(n):
            for i1 in range(n):
                for i2 in range(n):
                    for i3 in range(n):
                        for i4 in range(n):
                            keyGuessModified = [
                                score[0][i0][0], score[1][i1][0], score[2][i2][0], score[3][i3][0], score[4][i4][0]]
                            keyString = ''.join([chr(e)
                                                for e in keyGuessModified])
                            c = str(encrypt(encrypted, keyGuessModified))
                            s = classify(c)
                            if (s < 30):
                                print('{}\t\t{}'.format(keyString, s))
                                print(c)
                                print()
            # print()
            # print()
            # for j in range(len(keyGuessModified)):
            #     print(replaceEveryNth(
            #         encrypt(encrypted, keyGuessModified), 5, j, ' '))
            #     print()
            #     print()


if __name__ == '__main__':
    crack2(encrypted)
