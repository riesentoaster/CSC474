import base64

englishLetterFrequencies = [[b'E'[0], 0.13], [b'T'[0], 0.091], [b'A'[0], 0.082], [b'O'[0], 0.075], [b'I'[0], 0.07], [b'N'[0], 0.067], [b'S'[0], 0.063], [b'H'[0], 0.061], [b'R'[0], 0.06], [b'D'[0], 0.043], [b'L'[0], 0.04], [b'C'[0], 0.028], [b'U'[
    0], 0.028], [b'M'[0], 0.024], [b'W'[0], 0.024], [b'F'[0], 0.022], [b'G'[0], 0.02], [b'Y'[0], 0.02], [b'P'[0], 0.019], [b'B'[0], 0.015], [b'V'[0], 0.0098], [b'K'[0], 0.0077], [b'J'[0], 0.0015], [b'X'[0], 0.0015], [b'Q'[0], 0.00095], [b'Z'[0], 0.00074]]


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
        to_return[i] = cleartext[i] ^ key
    return bytes(to_return)


encrypted = decode("1JKGm5nUhpGXkZ2CnZqT1Jydh9SVgYydmJ2Vhp2Rh9r+/qysvaLaFnRgtZqAm5qdgYfUg5WH1JWA1ICcnYfUgJ2ZkdSVgNS2hoGakJ2HnYGZ2NSVmpDUhpGYjZ2ak9SbmtSAnJHUgpWYm4GG1JuS1Jydh9SAhpubhIfY1JebgpGGkZDUlZabgYDUh52MgI3Um5LUgJyR1JibmpPZlpuVgIfUlpGYm5qTnZqT1ICb1ICckdSZkZrZm5LZg5WG1IOdgJzUhJGagJybgYeRh9SVmpDUloGYg5WGn4fUm5LUnIGGkJiRh9jUlZqQ1ISBgNSbmtSWm5WGkNSAnJGZ1IeRmJGXgNSHm5iQnZGGh8/UlZqQ1JCdh4Sbh5GQ1ICckZnUh5GElYaVgJGYjdSVmJuak9SAnJHUh5ybhpHO1JWakNSBmpCRhtSAnJHUhIaRgJGMgNSbktSfkZGEnZqT1ICckdSHkZWZkZrUnZrUkYyRhpedh5HY1JyR1JuGkJGGkZDUgIOb1ICchpGR2ZaVmp+RkNSTlZiYkY2H2NSDnJ2XnNSckdSclZDUloGdmIDUlYDUtoaBmpCdh52BmdjUgJvUhpuD1ICb1ICckdSZm4GAnNSbktSAnJHUhJuGgNrUo5yRmtS4nZab1IeVg9SAnJGZ1JWQgpWal52ak9SWm5iQmI3UgJuDlYaQh9ScnZnY1JyR1IeRmoDUkp2CkdSSm4GG2ZaVmp+RkNSTlZiYkY2H1JWTlZ2ah4DUgJyRmdjUnZrUnJuEkYfUm5LUnZqAkYaXkYSAnZqT1ICckZna1KOckZrUgJyRh5HUl5WZkdSakZWG1JuBhtSHnJ2Eh9jUm4GG1IKRgJGGlZrUh5uYkJ2RhofUhpGAhpGVgJGQ1IOdgJydmtSAnJHUnJWGlpuBhtrUoJyR1JGakZmN2NSBhpORkNSWjdSAnJGdhtSRlZORhpqRh4fUgJvUl5WEgIGGkdSAnJGZ2NSEgYaHgZGQ1ICckZnUgZqTgZWGkJGQmI3P1JKbhtSdmoeAlZqAmI3UgJyR1JablYCH1JuS1LWagJuanYGH2NSbmtSV1JeRhoCVnZrUh52TmpWY2NSGm4ORkNSDnYCc1JOGkZWA1IKdm5iRmpeR1JKGm5nUlZiY1ISVhoCH1JWTlZ2ah4DUgJyR1JGakZmNz9SVmpDUlYDUgJyR1JKdhoeA1JeclYaTkdSAm5uf1JuakdSbktSAnJHUkpuBhtmWlZqfkZDUk5WYmJGNh9jUg52AnNSAnJHUh5GVmZGa1JWakNSZlYadmpGH2NSVmpDUkpuGl5GQ1ICckdSGkYeA1ICb1JKYkZHUkJ2Hk4aVl5GSgZiYjdrUvZrUlZCQnYCdm5rUgJvUgJydh9SYm4eH2NSAnJGN1IORhpHUhIaRgpGagJGQ1JKGm5nUk5GAgJ2ak9SDlYCRhtSWjdSAnJHUnJuGh5HUg5ydl5zUtZqAm5qdgYfUnJWQ1JCdh4Sbh5GQ1JWYm5qT1ICckdSHkZXZl5uVh4Da1LidlpvY1IKRjJGQ1JWA1ICckdSQnYeAhpGHh9SVmpDUkJ2Hk4aVl5HY1JCRhJWGgJGQ1JKGm5nUtoaBmpCdh52BmdjUlZqQ1JWWlZqQm5qRkNSAnJHUlpibl5+VkJHa/v6srKLaFnRgp5GCkYaVmNSZm5qAnIfUnJWQ1Jqbg9SRmJWEh5GQ2NSVmpDUg52agJGG1IOVh9SVmJmbh4DUk5uakdjUlZqQ1LeVkYeVhtOH1JiRk52bmofUlZqQ1IecnYSEnZqT1IORhpHUmpuA1JebmZ2ak9SAm9ScnZnUkoabmdS2hoGakJ2HnYGZ2NSVmpDUnJHUnZmVk52akZDUgJyVgNSHm5mR1JuEhJuGgIGanYCdkYfUnJWQ1JaRkZrUmpGTmJGXgJGQ2NSSm4bUgJyR1IOdmpCH1JyVkNSVgNSYkZWHgNSWkZGa1JuSgJGa1JKVgpuBhpWWmJHY1JWakNSckdSAnJuBk5yA1ICclYDUnJHUmYGHgNSAhoGHgNSAm9SAnJGZ1JWA1JiVh4Da1LWakNSAnJHUmJuak5GG1J2A1IOVh9SQkZKRhoaRkNjUgJyR1JmbhpHUkZWTkYbUg5GGkdSAnJuHkdSDnJvUl5uZmZWakJGQ1KSbmYSRjdOH1JKYkZGA1ICb1JOBlYaQ1ICckdSXm5WHgNjUlZqQ1IORhpHUmZuGkdSXm5qSnZCRmoDUm5LUhIaRgpGagJ2ak9SbgYbUk5GAgJ2ak9SVh4edh4CVmpeRztSAnJGN1IaRl5GdgpHUkoaRhYGRmoDUhpGEhpubkofUkoabmdSkm5mEkY3Ulo3UmJGAgJGG2NSAnJWA1JWH1ICckY3UnJWQ1JqbgNSEhpGCkZqAkZDUt5WRh5WG04fUlYaGnYKVmNSVgNSAnJHUkp2Gh4DY1ICckY3Uh5ybgZiQ1JWA1JiRlYeA1IeAm4TUgJyR1IaRmZWdmpCRhtSbktScnYfUlYaZjc7UlZqQ1ICckY3Ug5GGkdSRjISRl4CdmpPUgJyVgNSAnJHUh5GVh5ua1JKbhtSAhpWah4SbhoCdmpPUgIabm4SH1IObgZiQ1JaRl5uZkdSZm4aR1IGakpWCm4GGlZaYkdSRgpGGjdSQlY3Y1JWH1ICckdSDnZqQh9SThpGD")

myEncrypted = encode(encrypt(
    b'This is a long and complete english text that contains a few characters to check if my decoding algorithm works', 0x85))


def frequencyAnalysis(text):
    counts = dict.fromkeys(range(256), 0)
    letterCounts = {}
    for e in text:
        counts[e] += 1

    for key in counts:
        if key >= b'a'[0] and key <= b'z'[0]:
            counts[key-32] += counts[key]

    for key in counts:
        if key >= b'A'[0] and key <= b'Z'[0] and counts[key] > 0:
            letterCounts[key] = counts[key]

    if (len(letterCounts) < 5):
        return float('inf')

    for key in letterCounts:
        letterCounts[key] /= len(text)

    letterCounts = [[k, v] for [k, v] in letterCounts.items()]

    letterCounts = sorted(letterCounts, key=lambda e: e[1], reverse=True)

    score = 0

    for englishLetterIndex, [letter, value] in enumerate(englishLetterFrequencies):
        letterCountIndex = findInList(letterCounts, lambda x: x[0] == letter)
        if letterCountIndex == -1:
            score += 1
        else:
            score += abs(englishLetterIndex-letterCountIndex)*value

    return score


def crack(decodedText):
    scores = [[i, frequencyAnalysis(encrypt(decodedText, i))]
              for i in range(256)]

    scores = [e for e in scores if e[1] < float('inf')]

    scores = sorted(scores, key=lambda e: e[1])

    for e in scores[:3]:
        print('Decryption with key {}:'.format(hex(e[0])))
        print(encrypt(decodedText, e[0]))


crack(encrypted)
