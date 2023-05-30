 #!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data():
    data_path = os.path.join("out", "emotional_classification_filtered.csv")
    data = pd.read_csv(data_path, usecols=["title", "emo_label", "label"])
    return data

def plot_all_headlines(data):
    emotion_counts = data["emo_label"].value_counts()
    plt.bar(emotion_counts.index, emotion_counts.values)
    plt.xlabel("Emotions")
    plt.ylabel("Count")
    plt.title("Distribution of Emotions across all headlines")
    plt.xticks(rotation=45)
    plt.show()
    output_path = os.path.join("out", "emotion_all_headlines.png")
    plt.savefig(output_path)
    plt.close()
    
def plot_fake(data):
    fake_data = data[data["label"] == "FAKE"]
    emotion_counts = fake_data["emo_label"].value_counts()
    plt.bar(emotion_counts.index, emotion_counts.values)
    plt.xlabel("Emotions")
    plt.ylabel("Count")
    plt.title("Distribution of Emotions across FAKE headlines")
    plt.xticks(rotation=45)
    plt.show()
    output_path = os.path.join("out", "emotion_fake_headlines.png")
    plt.savefig(output_path)
    plt.close()

def plot_real(data):
    fake_data = data[data["label"] == "REAL"]
    emotion_counts = fake_data["emo_label"].value_counts()
    plt.bar(emotion_counts.index, emotion_counts.values)
    plt.xlabel("Emotions")
    plt.ylabel("Count")
    plt.title("Distribution of Emotions across REAL headlines")
    plt.xticks(rotation=45)
    plt.show()
    output_path = os.path.join("out", "emotion_real_headlines.png")
    plt.savefig(output_path)
    plt.close()
    
    
def main():
    data = load_data()
    plot_all_headlines(data)
    plot_fake(data)
    plot_real(data)

if __name__ == "__main__":
    main()


