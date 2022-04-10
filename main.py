
def primeChecker(number):
    isPrime = True

    for i in range(2, number):
        if number % i == 0:
            isPrime = False
    if isPrime:
        print("That is indeed a prime number")
    else:
        print("That is not a prime")


n = int(input("Check this number: "))
primeChecker(number=n)
