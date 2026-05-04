from main import is_even, is_palindrome


def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == False
    try:
        is_even("not an integer")
    except ValueError as e:
        assert str(e) == "Input must be an integer."    


def test_palindrome():
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("Hello") == False
    try:
        is_palindrome(123)
    except ValueError as e:
        assert str(e) == "Input must be a string."        