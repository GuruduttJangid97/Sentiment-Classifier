import csv
from sentiment import get_pos, get_neg
import matplotlib.pyplot as plt


# Reading Data from CSV file
with open("assets/project_twitter_data.csv") as file:
    reader = csv.DictReader(file)

    # Writing Data To CSV File
    with open("resulting_data.csv", mode="w", newline="", encoding="utf-8") as output_file:
        writer = csv.writer(output_file)

        # Writing Header To CSV File
        writer.writerow([
            "Number_Of_Retweets",
            "Number_of_Replies",
            "Positive_Scores",
            "Negative_Scores",
            "Net_Scores"
        ])

        # Iterate Sequence
        for row in reader:
            tweet_text = row["tweet_text"]
            retweet_count = int(row["retweet_count"])
            reply_count = int(row["reply_count"])

            positive_score = get_pos(tweet_text)
            negative_score = get_neg(tweet_text)

            net_score = positive_score - negative_score

            writer.writerow([
                retweet_count,
                reply_count,
                positive_score,
                negative_score,
                net_score
            ])


# To Generate Scatter Plot
retweets = []
net_scores = []

with open("resulting_data.csv") as file:
    reader = csv.DictReader(file)

    for data in reader:
        retweets.append(int(data["Number_Of_Retweets"]))
        net_scores.append(int(data["Net_Scores"]))


plt.scatter(retweets, net_scores)
plt.xlabel("Number of Retweets")
plt.ylabel("Net Score")
plt.title("Number of Retweets vs Net Score")
plt.savefig("scatter_plot.png", bbox_inches="tight")
plt.show()