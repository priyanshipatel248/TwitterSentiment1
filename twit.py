# cleaning code
import string
from collections import Counter
import matplotlib.pyplot as plt

import GetOldTweets3 as got


def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('donald trump') \
        .setSince("2019-05-01") \
        .setUntil("2020-09-01") \
        .setMaxTweets(200)
    # list of objects get stored in tweets object
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    # iterating through tweets list
    text_tweets = [[tweet.text] for tweet in tweets]
    return text_tweets


text = ""
text_tweets = get_tweets()
length = len(text_tweets)

for i in range(0, length):
    text = text_tweets[i][0] + " " + text
    # print(text)
# text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()

clean_text = lower_case.translate(str.maketrans(' ', ' ', string.punctuation))  # remove punctuation from string
# print(clean_text)
# tokenized word for NLP
# convert sentence into token

tokenized_word = clean_text.split()
# print(tokenized_word)  # print as list

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
# we need to remove this stop words it doesn't contain meaning
final_words = []

for word in tokenized_word:
    if word not in stop_words:
        final_words.append(word)
# print(final_words)

# NLP emotion algorithm
emotion_list = []
with open('emotion.txt', 'r')as file:
    for line in file:  # check if the word is present in final word and also present in emotion word
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        # print("word :" + word + " " + "Emotion :" + emotion)

        # if word is present add the emotion to emotion list
        if word in final_words:
            emotion_list.append(emotion)
print(emotion_list)
w = Counter(emotion_list)
print(w)

fig, axl = plt.subplots()
axl.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
