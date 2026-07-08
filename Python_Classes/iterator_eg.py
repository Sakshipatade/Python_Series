# below is the iterator created by our own.


class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.new_list = [i for i in self.sentence.split()]
        

    def __iter__(self):
        return self

    def __next__(self):
        for i in self.new_list:
            return i

my_sentence = Sentence('how are you?')
new = iter(my_sentence)






