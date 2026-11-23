def print_numbers(n):
    if n == 0: 
        return

    print_numbers(n - 1)  


print_numbers(5)

def factorial(n):

    if n == 0 or n == 1: 
        return 1

    return n * factorial(n - 1)


