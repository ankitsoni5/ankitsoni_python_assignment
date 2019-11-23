from com.ankit.utility.utilities import get_prime_series

while True:
    number = int(input('Enter the number to get the prime number series (press zero to exit) : '))
    if number == 0:
        break
    else:
        if number > 1:
            result = get_prime_series(number)
            print(result)
        else:
            print("Number should be greater than 1.")
