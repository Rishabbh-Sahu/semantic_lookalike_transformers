# -*- coding: utf-8 -*-
"""
@author: rishabbh-sahu
"""

def remove_next_line(txt_arr):
    '''
    data cleansing in order to remove next line symbol may arise while reading the file
    txt_arr: list [] - [[sequence of text1],[sequence of text2]...]
    return: cleaned text without next line '\n' char
    '''
    return [sub.replace('\n', '') for sub in txt_arr]

def remove_punctuations(txt_arr):
    '''
    data cleansing in order to remove various punctuations exits in the file
    txt_arr: list [] - [[sequence of text1],[sequence of text2]...]
    return: cleaned text without specified punctuations
    '''
    return txt_arr

def text_to_word_list(sentences):
    '''
    Huggingface Fast tokenizer accepts input as [['word1','word2'....'wordn']]
    Parameters-
    input: original form of sentences 
    return: sentences split into words by whitespace 
    '''
    return [s.split() for s in sentences]



