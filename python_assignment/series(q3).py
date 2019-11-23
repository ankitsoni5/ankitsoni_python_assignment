from com.ankit.utility.utilities import series

while True:
    number = int(input("Enter the number till you want to print the series (press zero to exit) : "))
    if number == 0:
        break
    if number < 0:
        print("Number should be greater than zero.")
    else:
        series(number)