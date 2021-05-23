def CaesarCipher(t, n, x):
    size = len(t)
    t = t.upper()
    # print(t)
    e = ''
    d = ''
    if x == 0:
        for i in range(size):
            e += chr(65 + (ord(t[i])-65+n)%26)
            # print(e)
        return e
    elif x == 1:
        for i in range(size):
            d += chr(65 + (ord(t[i])-65-n)%26)
            d = d.lower()
        return d

text = input()
Encyption = CaesarCipher(text, 3, 0)
print(Encyption)
Decryption = CaesarCipher(Encyption, 3, 1)
print(Decryption)
