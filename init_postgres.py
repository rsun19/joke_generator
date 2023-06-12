import json
import os
import psycopg2
from decouple import config

conn = psycopg2.connect(
        host="localhost",
        database="joke",
        user=config('USER'),
        password=config('PASSWORD')
)

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS jokes CASCADE;')
cur.execute('CREATE TABLE jokes (id serial PRIMARY KEY,'
                                 'joke text NOT NULL,'
                                 'sentiment numeric(10, 2),'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

cur.execute('DROP TABLE IF EXISTS cleanjokes CASCADE;')
cur.execute('CREATE TABLE cleanjokes (id serial PRIMARY KEY,'
                                 'joke text NOT NULL,'
                                 'sentiment numeric(10, 2),'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

with open('jokes_with_sentiment.json', 'r') as file:
    jokes_data = json.load(file)

for joke in jokes_data:
    cur.execute(
    "INSERT INTO jokes (joke, sentiment, date_added) VALUES (%s, %s, CURRENT_TIMESTAMP);",
    (joke['Joke'], joke['sentiment'])
)

with open('jokes_with_sentiment_clean.json', 'r') as file:
    jokes_data_clean = json.load(file)

for joke in jokes_data_clean:
    cur.execute(
    "INSERT INTO cleanjokes (joke, sentiment, date_added) VALUES (%s, %s, CURRENT_TIMESTAMP);",
    (joke['Joke'], joke['sentiment'])
)

conn.commit()
cur.close()
conn.close()