# # regular expression is a special text string which is used to find patterns in the data
# '''
#     we need to import the regular expression library

#     methods of regular expression (re) for finding data pattern and text manipulation are:
#     1.re.match(): it starts searching from start and returns <object,map(startPoint, endPoint), match = 'matched_string'>
#                 if no match found it return 'None' 
#                 (Note: it also matches spaces hence the string should be as it is including space or it will give None)

#     2.re.search(): it searches for the pattern throughout the text and return the first match that was found.
#                    it also returns an object with span and match. span is a tuple with the value of startingPoint
#                    and ending point of that found match.
#                    if no match founds it returns None 
            
#     3.re.findall(): it searches for pattern and returns list of founded items.
#                     if result is not match it returns None.
#                     it does not return the span but the list of matched items.

#     4.re.sub(): to replace a substring by another

# '''





# import re


# # re.match() examples 
# # text = 'Django is the framework of python'
# # result = re.match('Django is', text, re.I)
# # print(result)
# # Output =>>>     <re.Match object; span=(0, 23), match='Django is the framework'>


# # text_two = 'FastAPI is also library of python'
# # match = re.match('FastAPI isalso', text_two, re.IGNORECASE)
# # print(match)
# # here i removes the space between 'is' and 'also' so it does not match the original string hence return 'None'




# # re.search
# # sentence = 'i like to eat healthy food only because my first priority is to take care of my health. and being healthy'
# # result = re.search('take', sentence, re.I)
# # result_two = re.search('food on', sentence, re.I)
# # result_three = re.search('healthy', sentence, re.I)
# # print(result)
# # print(result_two)
# # print(result_three)
# # Note: if any word gets repeat it returns the first found word's match and span




# # re.findall()
# # txt = '''Python is the most beautiful language that a human being has ever created.
# #          I recommend python for a first programming language '''

# # result = re.findall('python', txt, re.I)
# # print(result)
# # here both python and Python are present but what if we want the Uppercase Python or wants both

# # result_two = re.findall('Python|python', txt)
# # print(result_two)

# # OR

# # result_three = re.findall('[Pp]ython', txt)
# # print(result_three)




# # re.sub()
# # txt = '''Python is the most beautiful language that a human being has ever created.
# # I recommend python for a first programming language'''
# # new_txt = re.sub('Python|python', 'javascript',txt, re.I)
# # OR
# # new_txt = re.sub('[Pp]ython', 'javascript', txt, re.I)
# # print(new_txt)


# # The following string is really hard to read unless we remove the % symbol.
# #  Replacing the % with an empty string will clean the text.

# # txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
# #           T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
# #           I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
# #           D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

# # new_match = re.findall('%', '', txt)
# # print(new_match)





# user_input = input('enter mail: ')
# regex_pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
# if re.match(regex_pattern, user_input):
#     print("Valid Email")
# else:
#     print('invalid email id')



num = 5
for i in range(num):
    for j in range(num-i):
        print('*', end=" ")
    print()
