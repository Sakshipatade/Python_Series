dog = {
    'name' : 'Beer',
    'color' : 'white',
    'breed' :'husky',
    'legs' : 4,
    'age' : 5
}

student = {
    'name' : {
        'first-name' : 'Sakshi',
        'last-name' : 'Patade'
    },
    'gender' : 'female',
    'age' : 21,
    'is_married' : False,
    'skills' : ['Python', 'Java', 'HTML', 'CSS', 'SQL'],
    'country' : 'India',
    'city' : 'pune',
    'address' : {
        'street' : 'High street balewadi',
        'pincode' : 411027
    }

}


print(len(student))

print(type(student.get('skills')))

student['skills'].extend(['React', 'Kotlin'])
print(student['skills'])

print(student.keys())
print(student.values())
dict_values = student.values()
print(dict_values)

print(student.items())
student.pop('is_married')
# print(student)

student.popitem()
# print(student)


del student['name']
print(student)
