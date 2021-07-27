from os import replace
from nltk.corpus.reader import wordnet
from numpy.lib.function_base import append, extract
import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


#convert xlxs to csv
# df = pd.read_excel('./files/Xenophobia.xlsx')
# df.to_csv('./files/xenophobia.csv')

# Read the tweets and place them in a dataframe
data_processed = pd.read_csv('./files/xenophobia.csv')
emotional_words = pd.read_csv('./files/emotion_words.csv')
emoji_category = pd.read_csv('files/emoji_category.csv')
emoticon_category = pd.read_csv('files/emoticon_category.csv')


# for each tweet and detect the emotion word
def get_emotion_words(tweet):
    words = []
    for word in tweet.split():
        if word in emotional_words['Emotion_Word'][0:-1].values:
            words.append(word)
    print(words)
    return words

# iterate over the tweets and get the emotion words
def get_emotion_words_list(tweets):
    words_list = []
    for tweet in tweets['Tweet']:
        words = get_emotion_words(tweet)
        words_list.append(words)
# append word_list to new column in dataframe
    tweets['Emotion_Words'] = words_list
    # tweets.to_csv('./files/data_processed.csv')
    return words_list
get_emotion_words_list(data_processed)

# # check for emotion word and replace with emotion category
def replace_emotion_words(tweet):
    words = []
    for word in tweet.split():
        if word in emotional_words['Emotion_Word'][0:-1].values:
            # words.append(word)
            # print(word)
            word = emotional_words[emotional_words['Emotion_Word'] == word]['Emotion_Category'].values[0]
            words.append(word)
            # print(words)
            tweet = tweet.replace(word, word)
    return words

# # iterate over the emotional word and replace with emotion category
def replace_emotion_words_list(data_with_emotion):
    words_list = []
    for tweet in data_with_emotion['Tweet']:
        words = replace_emotion_words(tweet)
        words_list.append(words)
    data_with_emotion['Emotional_Category'] = words_list
    # data_with_emotion.to_csv('./files/data_processed.csv')
    print(words_list)
    return(words_list)
replace_emotion_words_list(data_processed)

# for each tweet and detect the emoji
def get_emoji(tweet):
    emojis = []
    for emoji in tweet.split():
        if emoji in emoji_category['Emoji'].values:
            emojis.append(emoji)
    print(emojis)
    return emojis

# iterate over the tweets and get the emoji
def get_emoji_list(emojis):
    emoji_list = []
    for emoji in data_processed['Tweet']:
        emojis = get_emoji(emoji)
        emoji_list.append(emojis)
# append word_list to new column in dataframe
    data_processed['Emoji'] = emoji_list
    # data_processed.to_csv('./files/data_processed.csv')
    return emoji_list
get_emoji_list(data_processed)

# check for emoji and replace with emoji category
def replace_emoji(tweet):
    emojis = []
    for emoji in tweet.split():
        if emoji in emoji_category['Emoji'][0:-1].values:
            # words.append(word)
            # print(word)
            emoji = emoji_category[emoji_category['Emoji'] == emoji]['Category'].values[0]
            emojis.append(emoji)
            # print(words)
            tweet = tweet.replace(emoji, emoji)
    return emojis

# iterate over the emojis and replace with emoji category
def replace_emoji_list(data_processed):
    emoji_list = []
    for emoji in data_processed['Tweet']:
        emojis = replace_emoji(emoji)
        emoji_list.append(emojis)
    data_processed['Emoji_Category'] = emoji_list
    # data_processed.to_csv('./files/data_processed.csv')
    print(emoji_list)
    return(emoji_list)
replace_emoji_list(data_processed)

# for each tweet and detect the emoticon
def get_emoticon(tweet):
    emoticons = []
    for emoticon in tweet.split():
        if emoticon in emoticon_category['Emoticon'][0:-1].values:
            emoticons.append(emoticon)
    print(emoticons)
    return emoticons

 # iterate over the tweets and get the emoticons
def get_emoji_list(emoticon):
    emoticon_list = []
    for emoticon in data_processed['Tweet']:
        emoticon = get_emoticon(emoticon)
        emoticon_list.append(emoticon)
# append word_list to new column in dataframe
    data_processed['Emoticons'] = emoticon_list
    # data_processed.to_csv('./files/data_processed.csv')
    return emoticon_list
get_emoji_list(data_processed)

# check for emotion word and replace with emotion category
def replace_emoticon(tweet):
    emoticons = []
    for emoticon in tweet.split():
        if emoticon in emoticon_category['Emoticon'][0:-1].values:
            # words.append(word)
            # print(word)
            emoticon = emoticon_category[emoticon_category['Emoticon'] == emoticon]['Emoticon_Category'].values[0]
            emoticons.append(emoticon)
            # print(words)
            tweet = tweet.replace(emoticon, emoticon)
    return emoticons

# iterate over the emotional word and replace with emotion category
def replace_emoticon_list(data_processed):
    emoticon_list = []
    for emoticon in data_processed['Tweet']:
        emoticon = replace_emoticon(emoticon)
        emoticon_list.append(emoticon)
    data_processed['Emoticon_Category'] = emoticon_list
    data_processed.to_csv('./files/xenophobic_data_processed.csv')
    print(emoticon_list)
    return(emoticon_list)
replace_emoticon_list(data_processed)

# #replace emotion words with emotion category in tweets
# def replace_emotion_words(tweet):
#     words = []
#     for word in tweet.split():
#         if word in emotional_words['Emotion_Word'][0:-1].values:
#             words.append(word)
#             # print(words)
#             word = emotional_words[emotional_words['Emotion_Word'] == word]['Emotion_Category'].values[0]
#             tweet = tweet.replace(word, word)
#     return words
# print(replace_emotion_words(data_processed['Tweet'][0]))









