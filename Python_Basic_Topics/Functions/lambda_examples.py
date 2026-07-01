# double a number 

# double = lambda x:x*2
# print(double(5))
# print(double(12))

# return true if number is even else false

# is_even = lambda x:True if x%2==0 else False
# print(is_even(7))

# Sort this list by last name using lambda
# names = ["John Smith", "Alice Brown", "Charlie Adams"]

# sorted_items = sorted(names, key = lambda x:x[1] )
# print(sorted_items)
# understand this key wala concept




# Keep only positive numbers using filter() + lambda
# numbers = [3, -1, 7, -4, 0, 9, -2]

# positiveNumbers = list(filter(lambda x:x>=0, numbers))
# print(positiveNumbers)
# <filter object at 0x748bd03fef50> why this error when filter is used only



# Square every number using map() + lambda
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x:x**2, numbers))
# print(squared_numbers)


# Return "Fizz" if divisible by 3,
# "Buzz" if divisible by 5,
# "FizzBuzz" if both,
# else the number itself

# fizzbuzz = lambda x: 'Fizzubuzz' if x%3==0 and x%5==0 else 'Fizz'


