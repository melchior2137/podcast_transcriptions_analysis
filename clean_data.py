import re 
import os 

#load stopwords
with open("stopwords.txt", "r", encoding='utf-8') as file:
    stopwords = file.read()
stopwords = stopwords.split()

#text formatting and splitting
def split_str(text):
    invalid_char_pattern = r'[0-9!@^*()\'&%<>:.,"/\\|?*=#\[\]]'
    text = re.sub(invalid_char_pattern, '', text)
    text = text.lower()
    text = text.split()
    result = [word for word in text if word not in stopwords if not word.isnumeric()]
    return result

def clean_data(file_name):
    with open("data/{}".format(file_name), 'r', encoding='utf-8') as oldfile,\
    open("clean_data/{}.csv".format(os.path.splitext(file_name)[0]), 'w', encoding='utf-8') as newfile,\
    open("full_transcripts/full_transcript.csv", 'a', encoding='utf-8') as full_transcript,\
        open("full_transcripts/full_transcript_of_sentences.csv", 'a', encoding='utf-8') as full_transcript_of_sentences:
        lines = oldfile.read().splitlines(True)
        for line in lines[3:]:
            if "-->" not in line and line != "\n":
                full_transcript_of_sentences.write(line)
                line = split_str(line)
                for word in line:
                    newfile.write(word + '\n')
                    full_transcript.write(word+'\n')

def main():
    path_to_data = "data"
    file_list = os.listdir(path_to_data)
    if(os.path.isfile("full_transcripts/full_transcript.csv")):
        os.remove("full_transcript.csv")
    if(os.path.isfile("full_transcripts/full_transcript_of_sentences.csv")):
        os.remove("full_transcript_of_sentences.csv") #delete the transcripts file because it is in append mode


    for file_name in file_list:
        clean_data(file_name)


if __name__ == "__main__":
    main()