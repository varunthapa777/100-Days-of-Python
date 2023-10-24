def prime_checker(number):
    n = 2;
    ctr = 0
    while(number != n):
        if number%n == 0:
            ctr += 1
        n += 1
    if ctr == 0:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)