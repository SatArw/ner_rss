import pandas as pd
import feedparser
import requests
import json

from time import sleep
from functions import get_headlines, get_sentiment, get_summaries

# Dict of RSS feeds
newsurls = {
    'globenewswire-us': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
}

# Function to fetch the rss feed and return the parsed RSS
def parse_rss(rss_url):
    return feedparser.parse(rss_url)


# Lists to hold information about all articles
allheadlines = []
summaries = []
entities = []
RICs = []
topics = []
headline_sentiments = []
summary_sentiments = []

# Iterate over the feed urls
for key, url in newsurls.items():
    # Call get_eadlines() and combine the returned headlines with allheadlines
    allheadlines.extend(get_headlines(url))
    summaries.extend(get_summaries(url))

# Using the Thomson Reuters Intelligent Tagging API
# Sample content to send request to API
for i in range(len(allheadlines)):

    curr_entities = []
    curr_RICs = []
    curr_topics = []
    contentText = allheadlines[i]

    sleep(2)  # sleep time introduced so that we don't exceed the api calls limit
    headType = "text/raw"
    token = 'oSyQfYcRShExGJmJPXRgr4kOFAsIHqoJ'
    url = "https://api-eit.refinitiv.com/permid/calais"
    payload = contentText.encode('utf8')
    headers = {
        'Content-Type': headType,
        'X-AG-Access-Token': token,
        'outputformat': "application/json"
    }
    # The daily limit is 5,000 requests, and the concurrent limit varies by API from 1-4 calls per second.
    TRITResponse = requests.request("POST", url, data=payload, headers=headers)

    # Load content into JSON object
    JSONResponse = json.loads(TRITResponse.text)

    #Entities
    for key in JSONResponse:
        if ('_typeGroup' in JSONResponse[key]):
            if JSONResponse[key]['_typeGroup'] == 'entities':
                curr_entities.append(JSONResponse[key]['_type'] +
                                     ", " + JSONResponse[key]['name'])

    #RICs
    for entity in JSONResponse:
        for info in JSONResponse[entity]:
            if (info == 'resolutions'):
                for companyinfo in (JSONResponse[entity][info]):
                    if 'primaryric' in companyinfo:
                        symbol = companyinfo['primaryric']
                        curr_RICs.append(symbol)
 
    #Topics
    for key in JSONResponse:
        if ('_typeGroup' in JSONResponse[key]):
            if JSONResponse[key]['_typeGroup'] == 'topics':
                curr_topics.append(JSONResponse[key]['name'] + ", " +
                                   str(JSONResponse[key]['score']))

    entities.append(curr_entities)
    RICs.append(curr_RICs)
    topics.append(curr_topics)

#Analysing sentiments on headlines and summaries
for i in range(len(allheadlines)):
    headline_sentiments.append(get_sentiment(allheadlines[i]))
    summary_sentiments.append(get_sentiment(summaries[i]))

#Generating a dataframe with headlines, summaries, entities, RICs, topics, headline_sentiments and summary_sentiments as columns
headlines_dataframe = pd.DataFrame({"Headlines": allheadlines, "Summaries": summaries, "entities": entities, "RICs": RICs,
                                   "topics": topics, "headline_sentiments": headline_sentiments, "summary_sentiment": summary_sentiments})
print(headlines_dataframe)
