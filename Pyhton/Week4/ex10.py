low = int(input("Insert a low number:"))
high = int(input("Insert a high number:"))

def FizzBuzz(low, high):
    for n in range(low, high):
        if(n % 3 == 0):
            print("Fizz")
        if(n % 5 == 0):
            print("Buzz")
        if(n % 5 and n % 3 == 0):
            print("FizzBuzz")
FizzBuzz(low, high)
