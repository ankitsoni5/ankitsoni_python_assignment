def get_prime_series(n):
    result = [1]
    for num in range(2,n+1):
        if num > 1:
            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                result.append(num)
    return result

def is_palindrom(n):
    new_val = n[::-1]
    if n == new_val:
        return "Is Palindrom."
    else:
        return "Not a Palindrom"

def series(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            if i==j:
                print(3*i,end=" ")
            else:
                print("_",end=" ")
        print('\n')

