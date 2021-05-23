def createTable(key):
    default = ['A','B','C','D','E','F','G','H','IJ','K','L','M',
             'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    table = []
    if key == "":
        for i in range(5):
            table.append([])
            for j in range(5):
                table[i].append(default[i*5 + j])
    else:
        key = key.upper() # 대문자로 변환
        key = ''.join(dict.fromkeys(key)) # 중복 제거
        size = len(key)
        idx = 0
        cnt = 0
        for i in range(5):
            table.append([])
            for j in range(5):
                if size > 0:
                    table[i].append(key[idx])
                    default.remove(key[idx])
                    idx += 1
                    size -= 1
                else:
                    table[i].append(default[cnt])
                    cnt += 1
    return table

def PlayfairCipher(key, text, x):
    # only Encryption
    table = createTable(key)
    size = len(text)
    text = text.upper()
    text = text.replace('J', 'I') # I/J는 같은 문자로 취급
    copy = text[0] 
    result = ""
    x1, y1, x2, y2 = 0, 0, 0, 0
    for i in range(1, size): 
        if text[i-1] == text[i]: # 같은 문자열 사이 x 삽입
            copy += 'X'
        if text[i] == '': # 빈 칸 제거
            continue
        copy += text[i]
    if len(copy)%2 != 0: # 문자열 길이 짝수로 만들기
        copy += 'X'
    for j in range(0, len(copy), 2):
        for x in range(5):
            for y in range(5):
                if copy[j] in table[x][y]:
                    x1, y1 = x, y
                if copy[j+1] in table[x][y]:
                    x2, y2 = x, y
        if x1 == x2:
            y1 += 1
            y2 += 1
            if y1 >= 5: y1 = 0
            if y2 >= 5: y2 = 0
            result += (table[x1][y1]+table[x2][y2])
        elif y1 == y2:
            x1 += 1
            x2 += 1
            if x1 >= 5: x1 = 0
            if x2 >= 5: x2 = 0
            result += (table[x1][y1]+table[x2][y2])
        else:
            y1, y2 = y2, y1
            result += (table[x1][y1]+table[x2][y2])
    return result
        

print(PlayfairCipher(input(), input(), 1))
