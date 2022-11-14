"""
Write a Python program that checks if a string is a palindrome. Then  optionally  write  a  unit
test to check your program's correctness.
"""


def is_a_palindrome(string):
    if string == string[::-1]:
        return "It is a Palindrome"
    else:
        return "It is not a Palindrome"


print(is_a_palindrome("noon"))
print(is_a_palindrome("5335"))
print(is_a_palindrome("dogged"))
print(is_a_palindrome("kayak"))
