import tweepy
import json
from keys import twitter_api_key, twitter_api_secret, twitter_access_token, twitter_access_token_secret

auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

TWITTER_URL = "https://twitter.com"


def get_tweets(t_user):
    user = api.get_user(t_user)
    user_id = user._json["id"]
    latest_tweets = api.user_timeline(user_id=user_id, count=5, exclude_replies="true", include_trs="true")

    with open("news/rehposts.json") as reh_file:
        reh_data = json.load(reh_file)
        temp = reh_data["tweets_elon"]

    tweet_list = []
    new_ids = []
    for tweet in latest_tweets:
        if str(tweet._json["id"]) not in temp:
            tweet_list.append(f"{TWITTER_URL}/{t_user}/status/{tweet._json['id']}")
            new_ids.append(tweet._json["id"])

            for n in range(len(new_ids)):
                data_to_save = {
                    "tweets_elon": str(new_ids[n])
                }
                temp.append(data_to_save["tweets_elon"])
                with open("news/rehposts.json", "w") as reh_file:
                    json.dump(reh_data, reh_file, indent=4)

    return tweet_list
