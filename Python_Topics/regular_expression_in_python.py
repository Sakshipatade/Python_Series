# regular expression is a special text string which is used to find patterns in the data
'''
    we need to import the regular expression library

    methods of regular expression (re) for finding data pattern and text manipulation are:
    1.re.match(): it starts searching from start and returns <object,map(startPoint, endPoint), match = 'matched_string'>
                if no match found it return 'None' 
                (Note: it also matches spaces hence the string should be as it is including space or it will give None)

    2.re.search(): it searches for the pattern throughout the text and return the first match that was found.
                   it also returns an object with span and match. span is a tuple with the value of startingPoint
                   and ending point of that found match.
                   if no match founds it returns None 
            
    3.re.findall(): it searches for pattern and returns list of founded items.
                    if result is not match it returns None.
                    it does not return the span but the list of matched items.

'''





import re


# re.match() examples 
# text = 'Django is the framework of python'
# result = re.match('Django is', text, re.I)
# print(result)
# Output =>>>     <re.Match object; span=(0, 23), match='Django is the framework'>


# text_two = 'FastAPI is also library of python'
# match = re.match('FastAPI isalso', text_two, re.IGNORECASE)
# print(match)
# here i removes the space between 'is' and 'also' so it does not match the original string hence return 'None'




# re.search
# sentence = 'i like to eat healthy food only because my first priority is to take care of my health. and being healthy'
# result = re.search('take', sentence, re.I)
# result_two = re.search('food on', sentence, re.I)
# result_three = re.search('healthy', sentence, re.I)
# print(result)
# print(result_two)
# print(result_three)
# Note: if any word gets repeat it returns the first found word's match and span




# re.findall()
txt = '''Python is the most beautiful language that a human being has ever created.
         I recommend python for a first programming language '''

result = re.findall('python', txt, re.I)
# print(result)
# here both python and Python are present but what if we want the Uppercase Python or wants both

result_two = re.findall('Python|python', txt)
# print(result_two)

# OR

result_three = re.findall('[Pp]ython', txt)
print(result_three)
