
import math
while True:

    num1 = int(input("Enter first number: "))
    choice =input("Enter your operator: ")
    num2 = int(input("Enter second number: "))


    def add(a,b):
        return a + b
    def sub(a,b):
        return a - b
    def mul(a,b):
        return a * b
    def div(a,b):
            try:
                ans = a / b
            except Exception as e:
                 print(e)
                 ans = 0
            
            return ans

    
    if choice == "+":
        print("Addition: ",add(num1, num2))

    elif choice == "-":
        print("Substraction: ",sub(num1, num2))

    elif choice == "*":
        print("Multiplication: ", mul(num1, num2))

    elif choice == "/":
        print("Division: ", round(div(num1, num2)))

    else:
        print("Invalid Choice")
    


        

