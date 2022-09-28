from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    
def polarity0(num):
    polarity = "null"
    if(num == 0):
        polarity = "neutral"
    elif(num > 0):
        polarity = "positive"
    elif(num < 0):
        polarity = "negative" 
    return polarity

def polarity1(text):
    res = TextBlob(text)
    polarity = polarity0(res.sentiment.polarity)
    return polarity
    
def polarity2(text):
    sid_obj = SentimentIntensityAnalyzer()
    res = sid_obj.polarity_scores(text)
    polarity = polarity0(res["compound"])
    return polarity