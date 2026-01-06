from utility import checkPrime, findPrimes, count_digits, check_char

print("Welcome to CLI UTILITY SUITE")
print("1. Check if a number is prime")
print("2. Print all primes in a range")
print("3. Count digits of a number")
print("4. Check character type")

choice = int(input("Enter choice (1-4): "))

if choice == 1:
    n = int(input("Enter number: "))
    print("Prime" if checkPrime(n) else "Not Prime")

elif choice == 2:
    m = int(input("Enter start: "))
    n = int(input("Enter end: "))
    findPrimes(m, n)

elif choice == 3:
    n = int(input("Enter number: "))
    print(count_digits(n))

elif choice == 4:
    ch = input("Enter character: ")
    print(check_char(ch))

else:
    print("Invalid choice")
