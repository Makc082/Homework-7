def prime_number(number):

    if number <= 1:
        return False
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    else:
        return True
    
number = int(input("Enter your number: "))
if prime_number(number):
    print(f"Namber {number} prime!")
else:
    print(f"Number {number} not prime")