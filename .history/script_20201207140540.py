morse_code_dict = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def encrypt(message):
    cipher = ''
    for letter in message.upper():
        if letter != ' ':
            cipher += morse_code_dict[letter] + ' '
        else:
            cipher += ' '
    return cipher


def decrypt(message):
    message += ' '
    decipher = ''
    cipher_text = ''
    for letter in message:
        if letter != ' ':
            space = 0
            cipher_text += letter
        else:
            space += 1

            if space == 2:
                decipher += ' '
            else:
                decipher += list(morse_code_dict.keys()
                                 )[list(morse_code_dict.values()).index(cipher_text)]
                cipher_text = ' '
    return decipher


def run(morseToEnglish, textToTranslate):
    #
    # Write your code below; return type and arguments should be according to the problem's requirements
    #
    translatedText = None

    if morseToEnglish:
        translatedText = decrypt(textToTranslate)
        print(translatedText)
    else:
        translatedText = encrypt(textToTranslate)
        print(translatedText)


run(True, "- .... .   .-- .. --.. .- .-. -..   --.- ..- .. -.-. -.- .-.. -.--   .--- .. -. -..- . -..   - .... .   --. -. --- -- . ...   -... . ..-. --- .-. .   - .... . -.--   ...- .- .--. --- .-. .. --.. . -.. .-.-.- ")
