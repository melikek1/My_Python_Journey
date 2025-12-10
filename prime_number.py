print("Please enter a number: ")
number = int(input())

def is_prime(number):
    
    if number <= 1:
        print("invalid number")
        return

    
    if number == 2:
        print("is the smallest prime number")
        return

    
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            print("is not prime number")
            return  

    
    print("is prime number")


is_prime(number)