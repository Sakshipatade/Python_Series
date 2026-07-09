'''
Problem 1

Create a Student class.
Requirements:
class variable college = "ABC College"
instance variables: name, age
create a class method to change the college name.
create an instance method to display student details.
'''


class Student:

    college = 'ABC College'

    def __init__(self, name,age):
        self.name = name 
        self.age = age
    
    @classmethod
    def changeCollegeName(cls, college):
        cls.college = college
    
    def studentDetails(self):
        return f'Name : {self.name}\n Age : {self.age}\n College : {self.college}'
    

s1 = Student('Sakshi', 21)
s1.changeCollegeName('XYZ College')
print(s1.studentDetails())


