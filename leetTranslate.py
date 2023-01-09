leetLanguage = {
    'A':['λ'],
    'B':['ß'],
    'C':['('],
    'D':['đ'],
    'E':['ε'],
    'F':['ƒ'],
    'G':['6'],
    'H':['|-|'],
    'I':['!'],
    'J':['_|'],
    'K':['|<'],
    'L':['|_'],
    'M':['|V|'],
    'N':['|\\|'],
    'O':['0'],
    'P':['l³'],
    'Q':['0_'],
    'R':['я'],
    'S':['§'],
    'T':['†'],
    'U':['µ'],
    'V':['\\/'],
    'W':['VV'],
    'X':['><'],
    'Y':['¥'],
    'Z':['z']
}

array = []

def leetTranslate(string: str) -> str:
    result = ''

    for letter in string:
        if letter.upper() in leetLanguage:
            result += leetLanguage[letter.upper()][0]
            array.append(leetLanguage[letter.upper()][0])
        else:
            result += letter
            array.append(letter)
    return result

print(leetTranslate('Escribe un programa que reciba un texto y transforme lenguaje natural a "lenguaje hacker"'))
