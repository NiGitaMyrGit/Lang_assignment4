# Language assignment 4 - Using finetuned transformers via HuggingFace
This is the repository for the fourth assignment in the course Language Analytics from the bachelors elective course Cultural Data Science at Aarhus University

## 1. Contributions
## 2. Assignment description by instructor
In previous assignments, you've done a lot of model training of various kinds of complexity, such as training document classifiers or RNN language models. This assignment is more like Assignment 1, in that it's about *feature extraction*.

For this assignment, you should use ```HuggingFace``` to extract information from the *Fake or Real News* dataset that we've worked with previously.

You should write code and documentation which addresses the following tasks:

- Initalize a ```HuggingFace``` pipeline for emotion classification
- Perform emotion classification for every *headline* in the data
- Assuming the most likely prediction is the correct label, create tables and visualisations which show the following:
  - Distribution of emotions across all of the data
  - Distribution of emotions across *only* the real news
  - Distribution of emotions across *only* the fake news
- Comparing the results, discuss if there are any key differences between the two sets of headlines


## 2.1 Tips
- I recommend using ```j-hartmann/emotion-english-distilroberta-base``` like we used in class.
- Spend some time thinking about how best to present you results, and how to make your visualisations appealing and readable.
- **MAKE SURE TO UPDATE YOUR README APPROPRIATELY!**

## 3. Methods
For this text-classification of emotions the model [j-hartmann/emotion-english-distilroberta-base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base) from the HuggingFace Transformers library is used. This model is an extended version of sentiment analysis which not only labels/classifies the text with a postive and negative score, but instead base the score on different emotions.
The model labels/classifies and predicts 6 basic emotions (based on psychologist Paul Eckmans theory) and an additional neutral class. The emotion classes/labels are as follows:
  - 1. anger
  - 2. disgust
  - 3. fear
  - 4. joy
  - 5. neutral
  - 6. sadness
  - 7. surprise
It is a fintetuned version of the [distilroberta-base](https://huggingface.co/distilroberta-base) which reacehs an accuracy score of 91.3 % .
The huggingface Transformers library is a python library with a set of pretrained models used for Natural Language Understanding(NLU) and Natural Language Generation(NLG). 

## 4. Usage