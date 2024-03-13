"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    ...
    def __init__(self,path):
        word_file = open(path)
        self.words = self.parse(word_file)
        print(f'{len(self.words)} words read')
    
    def parse(self,word_file):
        '''breakdown the string of words into a list'''
        return [word.strip() for word in word_file]
    
    def random(self):
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    def parse(self,word_list):
        return [word.strip() for word in word_list if word.strip() and not word.startswith('#') ]


    
        
    