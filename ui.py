"""The UI of our program"""

from palindrome import palindrome


def ui()-> None:

    res = palindrome(word = input("Enter a word: "))
    print('Yes, is a palindrome!') if res else print('Nope, Try again')
