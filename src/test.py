#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline

emotion_classifier = pipeline("emotion", model="distilroberta-base", tokenizer="distilroberta-base")

df = pd.read_csv("dataset.csv")

df["emotion"] = df["title"].apply(lambda x: emotion_classifier(x)[0]["label"])

all_emotions = df["emotion"].value_counts(normalize=True)
fake_emotions = df[df["label"] == "fake"]["emotion"].value_counts(normalize=True)
real_emotions = df[df["label"] == "real"]["emotion"].value_counts(normalize=True)

emotions_df = pd.DataFrame({"All": all_emotions, "Fake": fake_emotions, "Real": real_emotions})
emotions_df.to_csv("emotion_distributions.csv")

emotions_df.plot(kind="bar", stacked=True)
plt.xlabel("Emotions")
plt.ylabel("Distribution")
plt.title("Emotion Distributions")
plt.legend()
plt.savefig("emotion_distributions.png")  # Save the plot as an image file
plt.show()
