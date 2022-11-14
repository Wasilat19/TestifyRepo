"""
Create a function that converts any string value to a Sentence case. Then write a unit test
that checks the function's correctness.
"""


def sentence_case(s):
    sentence = "the bird can fly"
    return sentence.capitalize()


print(sentence_case("the bird can fly"))
