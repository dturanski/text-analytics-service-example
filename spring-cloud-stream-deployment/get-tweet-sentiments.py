#!/usr/bin/env jython
'''
Parse a list of tweets, extract the text
'''
import json
import java.util.Arrays
import java.util.ArrayList

def input(payload):

	tweets=json.loads(str(payload))
	text = []
	
	for tweet in tweets:
		if tweet['lang'] == 'en':
			val = tweet['text'].encode('ascii','ignore')
			text.append(val)

	result = json.JSONEncoder().encode({"data": text })
	return result

def output(payload):
	if (payload):
		return java.util.ArrayList(java.util.Arrays.asList(payload))
	return None

data = processor.sendAndReceive(input(payload))

result = output(json.loads(data))


