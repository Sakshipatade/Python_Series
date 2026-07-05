# # below is the iterator created by our own.


# class Sentence:
#     def __init__(self, sentence):
#         self.sentence = sentence
#         self.new_list = [i for i in self.sentence.split()]
        

#     def __iter__(self):
#         return self

#     def __next__(self):
#         for i in self.new_list:
#             return i

# my_sentence = Sentence('how are you?')
# new = iter(my_sentence)


# class RangeExample:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.start < self.end:
            
        
    
# re = RangeExample(1, 10)
# print(next(re))
# print(next(re))

