def factorial(n):
    # if n is 1 or 0 return 1
    if n == 1 or n == 0:
        return 1
    # else return n*fact(n-1)
    return n*factorial(n-1)


if __name__ == '__main__':
    print(factorial(6))
