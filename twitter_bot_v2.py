import tweepy

print("My twitter bot is starting...")

CONSUMER_KEY = 'mMfyKALCanZAGKnfhGYAJJHAg'
CONSUMER_SECRET = 'JppXnwpaacOmRNVJe7YTO712lMYts76t6xzLCuG7JnxUPhX63R'

ACCESS_KEY = '1186821846529802240-qg5OlrLP76h8YKm6XnO1VumpWlqN4L'
ACCESS_SECRET = '02fV3hsphvJUriQOqQDQ2OYoHXFguMjvxsdtnrZZd2P7F'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

#Using api.mentions_timeline to retrieve mentions stream...
#>>> api.mentions_timeline()[0].__dict__.keys()
#    dict_keys(['_api', '_json', 'created_at', 'id', 'id_str', 'text',
#              'truncated', 'entities', 'source', 'source_url', 'in_reply_to_status_id',
#              'in_reply_to_status_id_str', 'in_reply_to_user_id', 'in_reply_to_user_id_str',
#              'in_reply_to_screen_name', 'author', 'user', 'geo', 'coordinates', 'place',
#               'contributors', 'is_quote_status', 'retweet_count', 'favorite_count', '
#               favorited', 'retweeted', 'lang'])

def fetch_last_seen_id(filename):
    f_read = open(filename, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, filename):
    f_write = open(filename, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    last_seen_id = fetch_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')

    for mention in reversed(mentions):
        print(str(mention.id) + '-' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#randomgif' in mention.full_text.lower():
            print('#hashtag detected... responding...')
            api.update_status('@' + mention.user.screen_name +
                '..tweetPayload...', mention.id)

while True:
    # Bot perpetually listens for an invocation
    reply_to_tweets()
    time.sleep(15)
