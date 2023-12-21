# classic way
def reverse_classic(n):
    reversedNumber = 0
    while n > 0:
        unit = n % 10
        n = n//10
        reversedNumber = reversedNumber*10 + unit
    print("reversed Number:", reversedNumber)


def reversePython(n):
    print("Reversed:", int(str(n)[::-1]))


if __name__ == "__main__":
    reverse_classic(2092)
    reversePython(2092)
