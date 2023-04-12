import pandas as pd
import os
import matplotlib.pyplot as plt

def main():

    word = "wiedźmin"
    path_to_data = "clean_data"
    file_list = os.listdir(path_to_data)
    dic = {}
    for file_name in file_list:
        occurences = 0
        with open("clean_data/{}".format(file_name), 'r', encoding='utf-8') as file:
            temp = file.read()
            dic[file_name[:-20]] = temp.count(word)
    series = pd.Series(dic)
    series.nlargest(10).plot(kind = 'barh', colormap = 'gray')
    print(series.nlargest(30))
    plt.tight_layout()
    plt.xlabel("Wystąpienia słowa \"wiedźmin\"")    
    # plt.savefig('img/witcher.svg', bbox_inches='tight')
    plt.show()



if __name__ == "__main__":
    main()