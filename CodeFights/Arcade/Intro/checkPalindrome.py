
#Given the string, check if it is a palindrome.


def check_palindrome(input_string):
    reverse = ""
    for c in input_string[::-1]:
        reverse = reverse + c

    if reverse == input_string:
        return True
    else:
        return False