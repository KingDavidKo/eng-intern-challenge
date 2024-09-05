import sys

letter_to_braille = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OO.O.O',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    'capital': '.....O',
    'number': '.O.OOO',
    ' ': '......',
    
}

braille_to_letter = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OO.O.O': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '.....O': 'capital',
    '.O.OOO': 'number',
    '......': ' '
}


def braille_to_text(string):
    output = ''
    capital_flag = False
    number_flag = False
    for i in range(len(string)//6):
        fragment = string[i*6:i*6+6]
        if braille_to_letter[fragment] == "capital":
            capital_flag = True
        
        elif braille_to_letter[fragment] == "number":
            number_flag = True
        else:
            if capital_flag == True:
                output += chr(ord(braille_to_letter[fragment]) - 32)
                capital_flag = False
            elif braille_to_letter[fragment] == " ":
                number_flag = False
                output += braille_to_letter[fragment]
            elif number_flag == True:
                if braille_to_letter[fragment] == "j":
                    output += "0"
                else:
                    output += chr(ord(braille_to_letter[fragment]) - 48)
            
            else:
                output += braille_to_letter[fragment]
    return output



def text_to_braille(string):
    output = ""
    number_flag = False
    for i in string:
        if ord(i) >= 65 and ord(i) <= 90:
            output += letter_to_braille["capital"]
            output += letter_to_braille[chr(ord(i)+32)]
        elif ord(i) >= 48 and ord(i) <= 57:
            if number_flag == False:
                output += letter_to_braille["number"]
                number_flag = True
            output += letter_to_braille[i]
        elif i == " ":
            number_flag = False
            output += letter_to_braille[" "]
        else:
            output += letter_to_braille[i]
        
    return output

def is_braille(text):
    if len(text) % 6 != 0:
        return False
    
    for i in text:
        if i != "O" and i != ".":
            return False
    
    for i in range(len(text)//6):
        
        if text[i*6:i*6+6] not in braille_to_letter:
            print(text[i*6:i*6+6])
            return False

    return True
n = len(sys.argv)
text = ''
for i in range(1, n):
    text += sys.argv[i]
    text += ' '
text = text[:-1]
if is_braille(text):
    print(braille_to_text(text))
   
else:

    print(text_to_braille(text))
