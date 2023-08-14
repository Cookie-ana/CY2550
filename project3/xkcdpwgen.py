#!/usr/bin/env python
# CY2550 Project3 Ananya Kumar

import argparse, random #will let me access command line arguments and generate random numbers/choose random words

# password generation logic and actions
def generate_password(words, caps, numbers, symbols):
    #opens up words.txt and puts all the words into a list
    file = open("words.txt", "r")
    wordlist = [word.strip() for word in file]
    file.close()

    selected_words = random.choices(wordlist, k=words)  #chooses the words amt of random words from the wordlist
    if caps > 0:    #capitalies caps amt of random words
        selected_words[:caps] = [word.capitalize() for word in selected_words[:caps]]

    password = "".join(selected_words)

    numberlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    symbollist = ["~", "!", "@", "#", "$", "%", "^", "&", "*", ".", ":", ";", "_"]
    # Add random numbers and symbols
    if numbers > 0:
        password += "".join(random.choices(numberlist, k=numbers))
    if symbols > 0:
        password += "".join(random.choices(symbollist, k=symbols))

    return password

def main():
    # Creates the parser
    parser = argparse.ArgumentParser(description="Generates secure, memorable passwords using the XKCD method") #same as mentioned in hw details
    # Adds the 5 arguments (example: parser.add_argument('--name', type=str, required=True))
    parser.add_argument("-w", "--words", type=int, default=4, help="include WORDS words in the password (default=4)")
    parser.add_argument("-c", "--caps", type=int, default=0, help="capitalize the first letter of CAPS random words (default=0)")
    parser.add_argument("-n", "--numbers", type=int, default=0, help="insert NUMBERS random numbers in the password (default=0)")
    parser.add_argument("-s", "--symbols", type=int, default=0, help="insert SYMBOLS random symbols in the password (default=0)")
    # Parses the argument
    args = parser.parse_args()

    # Does password generation using the given or parsed arguments
    password = generate_password(args.words, args.caps, args.numbers, args.symbols)
    print(password)

if __name__ == "__main__":
    main()