def fizz_buzz(num):
    num = int(input("Enter the number from 1 to 10: "))

    if num == 3:
        print("Fizz")
    elif num == 5:
        print("Buzz")
    elif num == 15:
        print("FizzBuzz")
    else:
        return num
    
    

fizz_buzz(input)