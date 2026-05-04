def is_even(num: int) -> bool:
    if not isinstance(num, int):
        raise ValueError("Input must be an integer.")
    if(num % 2 == 0):
        return True 
    else:
        return False
    

def is_palindrome(s: str) -> bool:
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    s = s.replace(" ", "").lower()
    return s == s[::-1]