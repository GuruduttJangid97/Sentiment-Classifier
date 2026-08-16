import csv
from sentiment import get_pos, get_neg

with open("assets/project_twitter_data.csv") as file:
    reader = csv.DictReader(file)

    with open("resulting_data.csv", mode="w", newline="", encoding="utf-8") as ouput_file:
        writer = csv.writer(ouput_file)

        writer.writerow([
            "Number of Retweets",
            "Number of Replies",
            "Positive Score",
            "Negative Score",
            "Net Score"
        ])

        for row in reader:
            Tweet_text = row['tweet_text']
            Retweet_count = int(row['retweet_count'])
            Reply_count = int(row['reply_count'])

            Positive_Score = get_pos(Tweet_text)
            Negative_Score = get_neg(Tweet_text)

            Net_Score = Positive_Score - Negative_Score

            writer.writerow([
                Retweet_count,
                Reply_count,
                Positive_Score,
                Negative_Score,
                Net_Score
            ])