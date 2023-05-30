 #!/usr/bin/env python3
# Huggingface pipeline
from transformers import pipeline 

# Data munging tools 
import pandas as pd
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def load_data():
    data_path = os.path.join("in", "fake_or_real_news.csv")
    data = pd.read_csv(data_path, usecols = ["title", "label"])
    return data

def load_pipeline():
    classifier = pipeline("text-classification",
                      model="j-hartmann/emotion-english-distilroberta-base", 
                      return_all_scores=False) # return emotion with highest value 
    return classifier

def remove_stopwords(data):
    stop_words = set(stopwords.words("english"))
    data["filtered_title"] = data["title"].apply(lambda x: " ".join([
        word for word in word_tokenize(x) if word.lower() not in stop_words]))
    return data

def emo_class(data, classifier):
    emo_list = []
    count = 0
    for filtered_title in data["filtered_title"]:
        data_titles = classifier(filtered_title)
        emo_titles = data_titles[0]["label"]
        emo_list.append(emo_titles)
        count +=1

    #adding the list as a column to the dataframe
    data["emo_label"] = emo_list

def main():
    nltk.download("punkt")
    nltk.download("stopwords")
    
    data = load_data()
    classifier = load_pipeline()
    data = remove_stopwords(data)
    emo_class(data, classifier)
    output_path = os.path.join("out", "emotional_classification.csv")
    data.to_csv(output_path, index=False)

if __name__ == "__main__":
    main()