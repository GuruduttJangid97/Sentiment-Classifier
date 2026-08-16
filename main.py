import csv
from sentiment import get_pos, get_neg

#Reading Data from CSV file 
with open("assets/project_twitter_data.csv") as file:
    reader = csv.DictReader(file)

#Writng Data To CSV File
    with open("resulting_data.csv", mode="w", newline="", encoding="utf-8") as ouput_file:
        writer = csv.writer(ouput_file)

#Writing Header To CSV File 
        writer.writerow([
            "Number of Retweets",
            "Number of Replies",
            "Positive Scores",
            "Negative Scores",
            "Net Scores"
        ])
#Iterate Sequence
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