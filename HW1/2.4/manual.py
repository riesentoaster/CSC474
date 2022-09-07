from twopointfour import encrypt, encrypted


# key = list(b'PPvBB')

# # for i in range(256):
# #     try:
# #         key[2] = 119
# #         key[1] = 87
# #         e = encrypt(encrypted, key).decode()
# #         # print(e)
# #         # print(e.index('am'))
# #         print(i, '\t\t', e[1940:1960])

# #         # print(e[1940])
# #     except:
# #         continue

# print(chr(87))
# print(chr(119))

print(encrypt(encrypted, b'PWwBB'))

# # key = list(b'PV$BB')
# # for i in range(32, 128):
# #     key[3] = i
#     print(encrypt(encrypted, key))
#     print()
