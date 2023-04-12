import pandas as pd
import os
import math
import matplotlib.pyplot as plt

def main():
    # load data
    df = pd.read_csv("clean_data/Zakaz social mediów dla dzieci [iDJl4KNtdhY].pl.csv")
    df.columns = ['words']

    # group and count occurences
    grouped_by_occurences = df.groupby('words').size()

    tf = grouped_by_occurences.to_dict()
    for key,value in tf.items():
        tf[key] = value/df.size

    path_to_data = "clean_data"
    file_list = os.listdir(path_to_data)
    number_of_docs = len(file_list)
    tfidf = {}

    for word in tf:
        occurences = 0
        for file_name in file_list:
            with open("clean_data/{}".format(file_name), 'r', encoding='utf-8') as file:
                temp = file.read()
                if(word in temp):
                    occurences+=1
                    continue
        print("{}: {}".format(word, math.log(number_of_docs/occurences, math.e)))
        tfidf[word] = tf[word] * math.log(number_of_docs/occurences, math.e)

    series = pd.Series(tfidf)
    series.nlargest(10).plot(kind = 'barh', colormap = 'gray')
    print(series.nlargest(30))
    plt.xlabel("word weight")
    plt.show()
if __name__ == "__main__":
    main()