import tweepy

print("My twitter bot is starting...")

CONSUMER_KEY = 'mMfyKALCanZAGKnfhGYAJJHAg '
CONSUMER_SECRET = 'JppXnwpaacOmRNVJe7YTO712lMYts76t6xzLCuG7JnxUPhX63R'

ACCESS_KEY = '1186821846529802240-qg5OlrLP76h8YKm6XnO1VumpWlqN4L'
ACCESS_SECRET = '02fV3hsphvJUriQOqQDQ2OYoHXFguMjvxsdtnrZZd2P7F'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#Use api.mentions_timeline to retrieve mentions stream..
