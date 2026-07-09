'''
Problem 1

Create a Student class.
Requirements:
class variable college = "ABC College"
instance variables: name, age
create a class method to change the college name.
create an instance method to display student details.
'''


# class Student:

#     college = 'ABC College'

#     def __init__(self, name,age):
#         self.name = name 
#         self.age = age
    
#     @classmethod
#     def changeCollegeName(cls, college):
#         cls.college = college
    
#     def studentDetails(self):
#         return f'Name : {self.name}\n Age : {self.age}\n College : {self.college}'
    

# s1 = Student('Sakshi', 21)
# s1.changeCollegeName('XYZ College')
# print(s1.studentDetails())


'''
Problem 2

Create a BankAccount class.

Requirements:

class variable = bank_name
constructor → account holder & balance
class method to change bank name
instance method to display account information

Create 3 accounts.

Change the bank name.

Observe how it changes for all accounts.
'''


# class BankAccount:

#     bank_name = 'Bank of India'

#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance

#     @classmethod
#     def changeBankName(cls, bank_name):
#         cls.bank_name = bank_name

#     def accountInfo(self):
#         print(f'Account Holder : {self.account_holder}\n Balance : {self.balance}\n Bank : {self.bank_name}')



# holder1 = BankAccount('Patrick', 100000)
# holder2 = BankAccount('Sandy', 90000)
# holder3 = BankAccount('Joy',95000)

# holder1.accountInfo()
# holder1.changeBankName('Bank of Maharashtra')
# holder1.accountInfo()

# holder2.accountInfo()
# holder2.changeBankName('HDFC Bank')
# holder2.accountInfo()

# holder3.accountInfo()
# holder3.changeBankName('State Bank of India')
# holder3.accountInfo()


'''
Problem 3

Create a class named Car.
Create a class variable

total_cars = 0

Every time a new object is created, increase total_cars.
Create a class method that returns the total number of cars.
'''

class Car:
    total_cars = 0

    def __init__(self):
        Car.total_cars += 1

    @classmethod
    def carCount(cls):
        return f'total numer of cars : {cls.total_cars}'
    
# print(Car.carCount())
c1 = Car()
c2 = Car()
c3 = Car()
c4 = Car()
c5 = Car()
c6 = Car()

print(Car.carCount())