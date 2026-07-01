def factorial_calculate(num):
    result = 1
    for i in reversed(range(1,num+1)):
        result = result * i
    print(result)
        
    
number = int(input('enter number: '))
factorial_calculate(number)