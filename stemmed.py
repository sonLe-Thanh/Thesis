import pandas as pd
import numpy as np
import csv

import string
import nltk
from nltk.corpus import stopwords

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

from nltk.tokenize import word_tokenize

country_name = ["China", "Japan", "Korea", "Vietnam", "France", "Germany"]

# data_file_name = ["Data/"+ country +"_processed.csv" for country in country_name]
# new_file_name = ["Data/" + country + "_stemmed.txt" for country in country_name]

ps = PorterStemmer()
wnl = WordNetLemmatizer()


class ProcessLine:
    def __init__(self):
        self.current_year = 2021

    def process_line(self, current_line):
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

        def lemmatizing(list_word):
            lemmatized = [wnl.lemmatize(word) for word in list_word]
            return ' '.join(token for token in lemmatized)

        def remove_date_review(current_line):
            if current_line[-1] == '"':
                # Get year of current line
                if len(current_line) > 5:
                    self.current_year = int(current_line[-5:-1])

                # Remove the year as normal
                k = 1
                reverse_string = current_line[::-1]
                while reverse_string[k] != '"':
                    k += 1
                current_line = reverse_string[k + 1:][::-1]
            elif current_line[-1].isdigit() and current_line[-2].isdigit() and current_line[-3].isdigit() and current_line[-4].isdigit():
                # Get the current year
                if len(current_line) > 5:
                    self.current_year = int(current_line[-4:])

                # Remove as normal
                k = 1
                reverse_string = current_line[::-1]
                while reverse_string[k] != ',':
                    k += 1

                k+=1

                while reverse_string[k] != ',':
                    k += 1
                current_line = reverse_string[k + 1:][::-1]
            if str(self.current_year) not in ["2020", "2021"]:
                self.current_year = "pre2020"
            # If not find any date, then assume this to be the current year
            return current_line[:-1]

        def remove_country_place(current_line):
            current_line = current_line[current_line.find(',') + 1:]
            return current_line[current_line.find(',') + 1:]


        current_line = remove_date_review(current_line)
        current_line = remove_country_place(current_line)
        current_line = punctuations_remove(current_line)
        current_line = stop_words_remove(current_line)
        current_line = lemmatizing(current_line)
        return current_line


    def process_file(self):
        for country in country_name:
            read_file_name = "Data/" + country + "_processed.csv"
            write_file_name_lemmatized = "Data/Lemmatized/" + country + "_lemmatized.txt"
            write_file_name_2021 = "Data/Timestamp/" + country + "_2021.txt"
            write_file_name_2020 = "Data/Timestamp/" + country + "_2020.txt"
            write_file_name_pre2020 = "Data/Timestamp/" + country + "_pre2020.txt"



            file_write = open(write_file_name_lemmatized, "a")
            file_read = open(read_file_name)
            lines = file_read.readlines()

            i = 1
            length_file = len(lines)
            while i < length_file - 1:
                curr_line = lines[i].strip("\n")
                for j in range(i + 1, length_file):
                    if lines[j][:len(country)] == country.lower():
                        curr_line = self.process_line(curr_line)
                        write_file_name_current = "Data/Timestamp/" + country + "_" + str(self.current_year) + ".txt"
                        file_write_current = open(write_file_name_current, "a")
                        file_write_current.write(curr_line + "\n")
                        file_write_current.close()
                        file_write.write(curr_line + "\n")
                        i = j
                        break
                    else:
                        curr_line += " " + lines[j].strip("\n")
            file_write.close()
            file_read.close()


processed_file = ProcessLine()
processed_file.process_file()
