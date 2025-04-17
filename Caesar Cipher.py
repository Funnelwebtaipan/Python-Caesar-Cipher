
#The Caesar Cipher

import pyperclip

#Message to be encrypted
message = 'I want to learn to hack in Python'

#Encryption/decrpytion key
key = 15

#Whether to encrypt or decrypt
mode = 'encrypt'

#Every possible symbol that can be encrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.@#$%^&*()_+*/-'

translated = ' '

#The encryption or decryption of the message
for symbol in message:
    #only symbols in SYMBOLS string can encrypted/decrypted
    if symbol in SYMBOLS:

        symbolIndex = SYMBOLS.find(symbol)

        #Performs encryption/decrpytion
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key
        
        #Handles wrap around
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated += SYMBOLS[translatedIndex]

    else:
        #Append the symbol without encrypting/decrypting
        translated += symbol

#Output the translated string
print(translated)
pyperclip.copy(translated)






