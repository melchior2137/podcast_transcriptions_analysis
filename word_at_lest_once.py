import pandas as pd
import os
import matplotlib.pyplot as plt

def main():

    word = "trochę"
    path_to_data = "clean_data"
    file_list = os.listdir(path_to_data)
    number_of_docs = len(file_list)
    occurences = 0
    for file_name in file_list:
        with open("clean_data/{}".format(file_name), 'r', encoding='utf-8') as file:
            text = file.read()
            if(word in text):
            # if(text.count(word) > 3):
                occurences+=1
    
    percentage = occurences/number_of_docs*100
    print("The word \"{}\" occured in {:.2f}% of podcasts".format(word, percentage))
if __name__ == "__main__":
    main()