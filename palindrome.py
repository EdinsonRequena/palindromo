"""The logic of our program """


def palindrome(word: str)-> bool:

    word.replace(' ', '').lower()
    return True if word == word[::-1] else False
