#!/usr/bin/env python3
import re
class MyString:
    def __init__(self, value = ""):
        
      self.value = value

    @property
    def value(self):
      return self._value

    @value.setter
    def value(self,value):
      if not isinstance(value, str):
        print("The value must be a string.")
      else:
        self._value = value

    def is_sentence(self):
      return self.value.endswith(".")
    
    def is_question(self):
       return self.value.endswith("?")
    
    def is_exclamation(self):
       return self.value.endswith("!")
    def count_sentences(self):
      sentences = re.split(r'[.!?]+\s*', self.value.strip())
      return len([num for num in sentences if num])
       

sentence = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
print(sentence.is_sentence())
print(sentence.is_question())
print(sentence.is_exclamation())
print(sentence.count_sentences())
