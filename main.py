import sys

def read_file():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
    #print(file_contents)
    word_count = file_contents.split()


if __name__ == '__main__':
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
    #print(file_contents)
    word_count = file_contents.split()

    lowc_file_contents = file_contents.lower()
    letters = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0
        ,"g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0
        , "n": 0, "o": 0, "q": 0, "p": 0, "r": 0, "s": 0, "t": 0
        , "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    
    for letter in lowc_file_contents:
        for dictletter in letters:
            if letter == dictletter:
                letters[dictletter] += 1
    
    print(f"--- Begin report of books/frankenstein.txt ---\n{len(word_count)} words found in the document")
    for dictletter in letters.items():
        print(f"The '{dictletter[0]}' character was found {dictletter[1]} times")
    print(f"--- End report ---")
