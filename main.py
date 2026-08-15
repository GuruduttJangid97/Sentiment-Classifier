import csv
from sentiment import get_pos, get_neg

with open("assets/project_twitter_data.csv") as file:
    reader = csv.DictReader(file)
    tweet_text = ""
    for row in reader:
        tweet_text += row['tweet_text']
    positive_score = get_pos(tweet_text)
    negative_score = get_neg(tweet_text)
    print(positive_score)
    print(negative_score)