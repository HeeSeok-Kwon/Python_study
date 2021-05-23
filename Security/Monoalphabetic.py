def Monoalphabetic(t, x):
    Encryption = {'a':'W','b':'M','c':'D','d':'A','e':'J','f':'L','g':'X','h':'Q','i':'Y','j':'B','k':'R','l':'C','m':'S',
                  'n':'E','o':'I','p':'H','q':'P','r':'F','s':'T','t':'K','u':'O','v':'N','w':'Z','x':'G','y':'U','z':'V'}
    Decryption = {'A':'d','B':'j','C':'l','D':'c','E':'n','F':'r','G':'x','H':'p','I':'o','J':'e','K':'t','L':'f','M':'b',
                  'N':'v','O':'u','P':'q','Q':'h','R':'k','S':'m','T':'s','U':'y','V':'z','W':'a','X':'g','Y':'i','Z':'w'}
    size = len(t)
    result = ""
    if x == 0:
        for i in range(size):
            result += Encryption[t[i]]
    elif x == 1:
        for i in range(size):
            result += Decryption[t[i]]
    return result

text = input()
encyption = Monoalphabetic(text, 0)
print(encyption)
decryption = Monoalphabetic(encyption, 1)
print(decryption)
