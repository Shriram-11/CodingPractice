# String
def pallindromeString(word):
    if word == word[::-1]:
        print("Is a pallindrome")
    else:
        print("not a pallindrome")


def pallindromeNumber(n):
    temp = n
    rev = 0
    while n > 0:
        unit = n % 10
        rev = rev*10+unit
        n = n//10
    if temp == rev:
        print("Is a pallindrome")
    else:
        print("Not a pallindrome")
