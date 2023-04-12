import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# create and display a word map


def plot_word_map(df):
    text = " ".join(x for x in df.words)
    mask = np.array(Image.open('img/cloud_img.jpg'))
    word_cloud = WordCloud(
        width=3000,
        height=2000,
        random_state=1,
        background_color="black",
        colormap="Wistia_r",
        mask=mask
    ).generate(text)

    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()


def plot_bar(grouped_by_occurences):
    grouped_by_occurences.nlargest(10).plot(kind='barh', colormap='gray')
    plt.xlabel("occurences")
    plt.tight_layout()
    plt.show()


def plot_pie(grouped_by_occurences):
    grouped_by_occurences.nlargest(10).plot(kind='pie', colormap = 'gray')
    plt.tight_layout()
    plt.show()


def main():
    # load data
    df = pd.read_csv("full_transcripts/full_transcript.csv")
    df.columns = ['words']

    # group and count occurences
    grouped_by_occurences = df.groupby('words').size()

    # print 10 most used words
    print(grouped_by_occurences.nlargest(10))
    print("{} records.".format(df.size))
    print("{} unique words.".format(grouped_by_occurences.size))

    plot_bar(grouped_by_occurences)
    plot_word_map(df)
    # plot_pie(grouped_by_occurences)


if __name__ == "__main__":
    main()
