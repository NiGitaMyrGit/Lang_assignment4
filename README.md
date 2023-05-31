# Language assignment 4 - Using finetuned transformers via HuggingFace
This is the repository for the fourth assignment in the course Language Analytics from the bachelors elective course Cultural Data Science at Aarhus University

## 1. Contributions
this code was written by me, but with help from this notebook [emotion-english-distilroberta-base](https://github.com/j-hartmann/emotion-english-distilroberta-base/blob/main/emotion_prediction_example.ipynb) found in the github repositroy related to the model 
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
For the text-classification of emotions the model [j-hartmann/emotion-english-distilroberta-base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base) from the HuggingFace Transformers library is used. It is a fintetuned version of the [distilroberta-base](https://huggingface.co/distilroberta-base) used for whole-sentences to make decisions eg. sequence classification, token classification or question/answering. The [distilroberta-base](https://huggingface.co/distilroberta-base) is a distilled version of the [roberta-base](https://huggingface.co/roberta-base) model, which is a pretrained model on English language, using self-supervised learning, meaning that no human labelling was done. The suelf-supervised learning was done with MLM (masked language modelling), where the model took around 15% of the words in the training data and masked them, in which is has to predict the masked words.

The [j-hartmann/emotion-english-distilroberta-base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base) model classifies the sentences into 6 basic emotions (based on psychologist Paul Eckmans theory) and has an additional neutral class. The emotion classes/labels are as follows:
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
The scripts where made in python 3.10.7. Should any errors occur, contrary to expectation, when running the script, please try to install this python version. 

### 4.1 Install packages
From the command line, make sure you are located in the main-directory. From here run the command `bash setup.sh`. This will install the packages, listed in the correct version, from the ```requirements.txt``` file.
### 4.2 Run the scripts
In order to run the scritps, make sure you are located in th main directory. From here run the command `python3 src/emo_classification.py`

## 5. Discussion of results
As can be seen in the folder ```out```, there are 4 files. Three of them are ```.png``` image files with barplots.
```emotion_all_headlines.png``` shows the distribution of the most prevalent emotions in all of the headlines. 
```emotion_fake_headlines.png``` shows the distribution of the most prevalent emotions the headlines classified as "fake news"
```emotion_real_headlines.png``` shows the distribution of the most prevalent emotions the headlines classified as "real news".
In general the top-4 emotional classes are the same whether for all the headlines, only the fake or only the real. The top most prevalent class is the 'neutral' class, which means that most of the headlines has been classified as neutral. 
The second most prevalent class category is "fear", though more in the real headlines than the fake headlines.The top third is 'anger', approximately the same for the real and fake headlines.
The top fourth is 'sadness', with slightly more in the real headlines than the fake headlines. 
For the last, and least present, three feelings: "joy, surprise, disgust" it is not the same order for any of the plots. Joy takes the fifth place for all headlines and the real ones, where as 'disgust' is placed 5th in the fake headlines plot, and joy as the least prevalent. 'Disgust' is for the real headliens palced in the seventh and last place. 
So as a conclusion real news headlines are slightly more joyful and fake ones more disgusting?
Though most prevalent, no matter what is fear, which is food for thought. Why are news so fearful and more seldomnly joyful? Perhaps real news are also a bit fake, not in their facts, but in their distribution of emotions.
 
