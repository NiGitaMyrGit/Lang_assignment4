#!/usr/bin/env python3
#import packages
import os
from transformers import pipeline
import pandas as pd
import tensorflow as tf

classifier = pipeline("text-classification", 
                      model="j-hartmann/emotion-english-distilroberta-base", 
                      return_all_scores=True)

# loading in the data
filename = os.path.join("in", "fake_or_real_news.csv")
# load into dataframe with only the headlines
data = pd.read_csv(filename)["title"]

data.shape
exit()


def main():
    docs=load_data()

#calling main function
if __name__== "__main__":
    main()