def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def findPrimes(m, n):
    for i in range(m, n + 1):
        if checkPrime(i):
            print(i)


def count_digits(n):
    return len(str(abs(n)))


def check_char(ch):
    if ch.islower():
        return "Small case"
    elif ch.isupper():
        return "Capital case"
    elif ch.isdigit():
        return "Digit"
    else:
        return "None"
