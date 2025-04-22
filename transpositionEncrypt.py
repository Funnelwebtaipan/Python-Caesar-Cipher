# Transposition Cipher
# By Al Sweigart
# For educational and learning purposes

import pyperclip

def main ():
    myMessage = 'Allan is learning to hack and Python and buying pentesting gear'
    myKey = 8

    cipherText = encryptMessage(myKey, myMessage)

    # Print the encrypted string in ciphertext to the screen, with
    # a | ("pipe" character) after it in case there are spaces at
    # the end of the encrypted message:
    print(cipherText + '|')

    #Copy the encrypted string in cipher text to the clipboard:
    pyperclip.copy(cipherText)

def encryptMessage(key, message):
    # Each string in ciphertext represents a column in the grid:
    ciphertext = [''] * key

    # Loop through each column in the ciphertext:
    for column in range(key):
        currentIndex = column

        # Keep looping until currentIndex goes past the message length:
        while currentIndex < len(message):
            # Place the character at currentIndex in message at the
            # end of the current column in the ciphertext list:
            ciphertext[column] += message[currentIndex]

            # Move current index over:
            currentIndex += key

    # Convert the ciphertext list onto a single string value and return it:
    return ''.join(ciphertext)

#if transpositionEncrypt.py is run(instead of imported as a module) call
# the main () function:
if __name__ == '__main__':
    main()