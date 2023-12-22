def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1)+fib(n-2)


def printSeries(n):
    a, b = 0, 1
    print(a, ",", b, end=" , ")
    for i in range(2, n):
        a, b = b, a+b
        print(b, end=" , ")


print(fib(5))
printSeries(5)
