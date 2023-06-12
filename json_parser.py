import json
import spacy
from textblob import TextBlob

with open('jokes.json', 'r') as file:
    jokes_data = json.load(file)

for joke in jokes_data:
    blob = TextBlob(joke['Joke'])
    sentiment = blob.sentiment.polarity
    joke['sentiment'] = sentiment

with open('jokes_with_sentiment.json', 'w') as file:
    json.dump(jokes_data, file)

with open('jokes (1).json', 'r') as file:
    jokes_data_clean = json.load(file)

for joke in jokes_data_clean:
    blob = TextBlob(joke['Joke'])
    sentiment = blob.sentiment.polarity
    joke['sentiment'] = sentiment

with open('jokes_with_sentiment_clean.json', 'w') as file:
    json.dump(jokes_data, file)