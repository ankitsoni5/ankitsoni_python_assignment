from com.ankit.utility.utilities import is_palindrom

while True:
    i = input("Enter the value to check for palindrom (press q to exit) : ")
    inew = i.replace(" ","")
    if inew == 'q':
        break
    if len(inew) <= 1:
        print("Inserted characters/numbers should be more than one.")
    else:
        result = is_palindrom(inew)
        print(result)