import feedparser
from textblob import TextBlob
import re

# Function to fetch the rss feed and return the parsed RSS
def parse_rss(rss_url):
    return feedparser.parse(rss_url)

# Function grabs the rss feed headlines (titles) and returns them as a list
def get_headlines(rss_url):
    headlines = []
    feed = parse_rss(rss_url)
    for newsitem in feed['items']:
        headlines.append(newsitem['title'])
    return headlines


def get_summaries(rss_url):
    summaries = []
    feed = parse_rss(rss_url)
    for newsitem in feed['items']:
        summaries.append(newsitem['summary'])
    return summaries


def get_entries(rss_url):
    entries = []
    feed = parse_rss(rss_url)
    for newsitem in feed['items']:
        entries.append(newsitem.keys())
    return entries

#Function to perform sentiment analysis
def get_sentiment(txt):
    # clean text
    clean_txt = ' '.join(
        re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", txt).split())
    # create TextBlob object of passed tweet text
    analysis = TextBlob(clean_txt)
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'