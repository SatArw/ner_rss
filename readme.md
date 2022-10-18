This repository illustrates analysis on RSS news feeds using some publicly available APIs. 

1. **Fetch news** - read in news source via an RSS feed (using feedparser)

2. **Extract Entities** - perform named enttity recognition (NER) on the unstructured text using the **Thomson Reuters Intelligent Tagging(TRIT)** API  

3. **Sentiment analysis** - perform sentiment analysis on the headlines and summaries using **Textblob**

4. **Creating a DataFrame** - Generate a dataframe with headlines, summaries, entities, RICs, topics, headline_sentiments and summary_sentiments as columns

Some of the libraries/dependancies to download before using this

1. Pandas

2. feedparser

3. requests

4. json

5. textblob

6. re