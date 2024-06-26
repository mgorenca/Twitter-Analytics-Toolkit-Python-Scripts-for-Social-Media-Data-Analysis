import tweepy

# Set up your Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Fetch 10,000 tweets (adjust count as needed)
tweets = tweepy.Cursor(api.search, q='*', count=10000).items()

# Initialize a dictionary to store the count of tweets for each language
language_count = {}

# Iterate through tweets and count languages
for tweet in tweets:
lang = tweet.lang
if lang in language_count:
language_count[lang] += 1
else:
language_count[lang] = 1

# Display the count for each language
for lang, count in language_count.items():
print(f"{lang}: {count}")

# Calculate percentage if needed
total_tweets = sum(language_count.values())
for lang, count in language_count.items():
percentage = (count / total_tweets) * 100
print(f"{lang}: {percentage:.2f}%")


import tweepy

# Set up your Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Fetch 10,000 tweets (adjust count as needed)
tweets = tweepy.Cursor(api.search, q='*', count=10000).items()

# Initialize counters
total_tweets = 0
retweet_count = 0

# Iterate through tweets and check for retweets
for tweet in tweets:
total_tweets += 1
if tweet.text.startswith("RT"):
retweet_count += 1

# Calculate the percentage of retweets
percentage_retweets = (retweet_count / total_tweets) * 100

# Display the results
print(f"Total tweets: {total_tweets}")
print(f"Retweets: {retweet_count}")
print(f"Percentage of retweets: {percentage_retweets:.2f}%")


import tweepy

# Set up your Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Fetch 10,000 tweets (adjust count as needed)
tweets = tweepy.Cursor(api.search, q='*', count=10000).items()

# Initialize counters
total_tweets = 0
extended_tweet_count = 0

# Iterate through tweets and check for extended tweets
for tweet in tweets:
total_tweets += 1
# Check if the tweet has extended content
if 'extended_tweet' in tweet._json:
extended_tweet_count += 1

# Calculate the percentage of extended tweets
percentage_extended_tweets = (extended_tweet_count / total_tweets) * 100

# Display the results
print(f"Total tweets: {total_tweets}")
print(f"Extended tweets: {extended_tweet_count}")
print(f"Percentage of extended tweets: {percentage_extended_tweets:.2f}%")


import tweepy

# Set up your Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Replace 'username_of_interest' with the actual Twitter handle you are interested in
username_of_interest = 'username_of_interest'

# Get user information
user = api.get_user(screen_name=username_of_interest)

# Display basic account information
print(f"ID: {user.id}")
print(f"Name: {user.name}")
print(f"Screen Name: {user.screen_name}")
print(f"Description: {user.description}")


import tweepy

# Set up your Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Replace 'username_of_interest' with the actual Twitter handle you are interested in
username_of_interest = 'username_of_interest'

# Get user timeline
tweets = api.user_timeline(screen_name=username_of_interest, count=10)

# Display the last 10 tweets
for tweet in tweets:
print(f"{tweet.user.screen_name}: {tweet.text}")
print("------")
