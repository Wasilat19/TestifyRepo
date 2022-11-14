import challenge2
import challenge9
import challenge10
import challenge5


def test_power():
    assert challenge2.power_of_num(5, 2) == 25


def test_uppercase():
    assert challenge9.to_upper("beauty") == "BEAUTY"


def test_sentence_case():
    assert challenge10.sentence_case("the bird can fly") == "The bird can fly"


def test_palindrome():
    assert challenge5.is_a_palindrome("noon") == "It is a Palindrome"
    assert challenge5.is_a_palindrome("5335") == "It is a Palindrome"
    assert challenge5.is_a_palindrome("dogged") == "It is not a Palindrome"
    assert challenge5.is_a_palindrome("kayak") == "It is a Palindrome"
