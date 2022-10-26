This repository illustrates analysis on RSS news feeds using some publicly available APIs. 

1. **Fetch news** - read in news source via an RSS feed (using feedparser)

2. **Extract Entities** - perform named enttity recognition (NER) on the unstructured text using the **Thomson Reuters Intelligent Tagging(TRIT)** API  

3. **Sentiment analysis** - perform sentiment analysis on the headlines and summaries using **Textblob**

4. **Creating a DataFrame** - Generate a dataframe with headlines, summaries, entities, RICs, topics, headline_sentiments and summary_sentiments as columns

 You should first install the requirements by running the following code:
 ``` pip install -r requirements.txt ```
 
