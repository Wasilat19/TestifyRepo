"""
Write a function that removes repeated characters from a string.
Sample Strings are:
a.Hello: output should be Helo
b.Concatenate: output should be Conaten
"""


def remove_repeated_characters(string):
    result = ""
    for char in string:
        if char not in result.casefold():
            result += char
    print(result)


remove_repeated_characters("Hello")
remove_repeated_characters("Concatenate")


