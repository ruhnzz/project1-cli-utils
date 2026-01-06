print("Welcome to CLI UTILITY SUITE:")
print("here we offer you:\n1.Check if a number is prime\n2.Print all primes in a range\n3.Count digits of a number\n4.Check character type (upper/lower/digit)")
choice = int(input("Enter choice(1-4):"))
if(choice==1):
    print("Let's check whether the number is Prime or Not")
    n = int(input("Enter Number: "))
    print(checkPrime(n))
elif(choice==2):
    print("Lets print all the Primes in a range")
    m = int(input("Enter Number1: "))
    n = int(input("Enter Number2: "))
    findPrimes(m,n)
elif(choice==3):
    print("Lets count no.of digits")
    n = int(input("Enter Number: "))
    print(count(n))
else:
    print("Let print the type")
    n = input("Enter: ")
    print(find(n))


