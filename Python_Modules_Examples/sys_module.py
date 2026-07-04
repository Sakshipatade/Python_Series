import sys

text = 'Sakshi'
roll_number = 43
hobbies = ['reading','singing', 'swiming']

print(sys.getsizeof(text))
print(sys.getsizeof(roll_number))
print(sys.getsizeof(hobbies))



''' The sys.getsizeof() method in Python returns the total memory size of an object in bytes.
 It is primarily used for memory profiling, debugging, and optimizing data structures to see exactly how much RAM an application consumes.'''
