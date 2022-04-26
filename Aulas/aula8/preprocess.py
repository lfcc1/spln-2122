import pandas as pd
import csv
import re

df = pd.read_csv('Tweets_pt_pt.csv')

df = df[['sentiment','tweet_text']]

df['sentiment'] = df['sentiment'].map('__label__{}'.format)

df['tweet_text'] = df['tweet_text'].map(lambda x: re.sub(r":\s*[˜'´-]?\s*([()DpP])+",' ',x))
df['tweet_text'] = df['tweet_text'].map(lambda x: re.sub(r"@\w+",' ',x))
df['tweet_text'] = df['tweet_text'].map(lambda x: re.sub(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)",' ',x))

# with open('tweets.txt', 'w') as f:
#     for index, row in df.iterrows():
#         f.write(f"{row['sentiment']} {row['tweet_text']}\n")

df.to_csv('tweets.csv', index=False, sep='\t', header=False, quoting=csv.QUOTE_NONE)