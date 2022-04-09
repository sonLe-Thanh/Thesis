import pandas as pd
import numpy as np
import csv

import string
import nltk
from nltk.corpus import stopwords

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

country_name = ["China", "Japan", "Korea", "Vietnam", "France", "Germany"]

# data_file_name = ["Data/"+ country +"_processed.csv" for country in country_name]
# new_file_name = ["Data/" + country + "_stemmed.txt" for country in country_name]

ps = PorterStemmer()


def process_line(current_line):
    def punctuations_remove(sentence):
        return sentence.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation))).lower()

    def stop_words_remove(sentence):
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(sentence)
        filtered_sentence = [word for word in word_tokens if not word in stop_words]
        return filtered_sentence

    def stemming(list_word):
        stemmed = [ps.stem(word) for word in list_word]
        return ' '.join(token for token in stemmed)

    def remove_date_review(current_line):
        if current_line[-1] == '"':
            k = 1
            reverse_string = current_line[::-1]
            while reverse_string[k] != '"':
                k += 1
            current_line = reverse_string[k + 1:][::-1]
        return current_line[:-1]

    def remove_country_place(current_line):
        current_line = current_line[current_line.find(',') + 1:]
        return current_line[current_line.find(',') + 1:]


    current_line = remove_date_review(current_line)
    current_line = remove_country_place(current_line)
    current_line = punctuations_remove(current_line)
    current_line = stop_words_remove(current_line)
    current_line = stemming(current_line)
    return current_line


def process_file():
    for country in country_name:
        file_name = "Data/" + country + "_processed.csv"
        write_file_name = "Data/" + country + "_stemmed.txt"
        file_write = open(write_file_name, "a")
        file_read = open(file_name)
        lines = file_read.readlines()

        i = 1
        length_file = len(lines)
        while i < length_file - 1:
            curr_line = lines[i].strip("\n")
            for j in range(i + 1, length_file):
                if lines[j][:len(country)] == country.lower():
                    curr_line = process_line(curr_line)
                    file_write.write(curr_line + "\n")
                    i = j
                    break
                else:
                    curr_line += " " + lines[j].strip("\n")
        file_write.close()
        file_read.close()


process_file()
