# -*- coding: utf-8 -*-

'''
sentiment_service.py
~~~~~~~~~~~~~~~~~~~~

App implements a sentiment analysis pipeline. 

'''
import cPickle
import os
import pandas as pd
import requests
import sklearn
import json
import sys
import warnings
from springcloudstream.stream import Processor

warnings.filterwarnings("ignore")

resp = requests.get("https://raw.githubusercontent.com/crawles/gpdb_sentiment_analysis_twitter_model/master/twitter_sentiment_model.pkl")
resp.raise_for_status()
cl = cPickle.loads(resp.content)

def regex_preprocess(raw_tweets):
    pp_text = pd.Series(raw_tweets)

    user_pat = '(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)'
    http_pat = '(https?:\/\/(?:www\.|(?!www))[^\s\.]+\.[^\s]{2,}|www\.[^\s]+\.[^\s]{2,})'
    repeat_pat, repeat_repl = "(.)\\1\\1+",'\\1\\1'

    pp_text = pp_text.str.replace(pat = user_pat, repl = 'USERNAME')
    pp_text = pp_text.str.replace(pat = http_pat, repl = 'URL')
    pp_text.str.replace(pat = repeat_pat, repl = repeat_repl)
    return pp_text

def process(data):
    doc = json.loads(data)
    X = regex_preprocess(doc["data"])
    prediction = cl.predict_proba(X)[:][:, 1]
    return json.dumps({"polarity" : prediction.tolist()})

Processor().start(process)

