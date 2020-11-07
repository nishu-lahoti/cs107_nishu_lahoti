import sys
sys.setrecursionlimit(2000) 
from linked_list import LinkedList, Nil

def get_list_of_sentences(chapter1 = 'swansway-chapter1.txt'):
    def to_sentences(p):
        for delimiter in '.?!': p = p.replace(delimiter, '|')
        return [s.strip('\"') for s in p.split ('|')]
    with open(chapter1, 'r', encoding = 'UTF-8') as f:
        paragraphs = f.readlines()

    sentences = [s for p in paragraphs for s in to_sentences(p) if len(s) > 1]
    list_of_sentences = Nil()
    for s in sentences[::-1]:
        list_of_sentences = list_of_sentences.prepend(s)

    return list_of_sentences

def longest_sentence(): # For some reason this is returning only a medium length sentence
    list_of_sentences = get_list_of_sentences()
    split_sentences = list_of_sentences.for_each(str.split)
    
    def longest(a, b): # our "combine" function
        return a if a > b else b
        
    longest_sentence = split_sentences.reduce_right(longest)
    length = len(longest_sentence)

    return length