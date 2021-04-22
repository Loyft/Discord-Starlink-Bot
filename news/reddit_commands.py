import praw
import json
from keys import *

R_CLIENT_ID = reddit_client_id
R_CLIENT_SECRET = reddit_client_secret
R_USERNAME = reddit_username
R_USER_AGENT = reddit_user_agent

reddit = praw.Reddit(client_id=R_CLIENT_ID,
                     client_secret=R_CLIENT_SECRET,
                     user_agent=R_USER_AGENT,
                     check_for_async=False)


def get_top(sub_red, interval):
    subreddit = reddit.subreddit(str(sub_red)).top(interval)

    current_top_score = 0
    top_sub = {}
    with open("news/rehposts.json") as past_reddit_posts_file:
        data = json.load(past_reddit_posts_file)
        temp = data[str(sub_red)]
        for submission in subreddit:
            if submission.score > current_top_score:
                if submission.url not in data[str(sub_red)]:
                    top_sub = submission
                    current_top_score = submission.score

                    data_to_save = {
                        str(sub_red): top_sub.url
                    }
                    temp.append(data_to_save[str(sub_red)])

                    with open("news/rehposts.json", "w") as past_reddit_posts_file:
                        json.dump(data, past_reddit_posts_file)

    return top_sub
