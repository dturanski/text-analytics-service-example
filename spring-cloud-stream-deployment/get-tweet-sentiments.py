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


#convert array of dict to array of str to java.util.ArrayList
def output(payload):

	if (payload):
		items = []
		data = json.loads(payload)
		for item in data:
			items.append(json.dumps(item))

		return java.util.ArrayList(java.util.Arrays.asList(items))
	return None

data = processor.sendAndReceive(input(payload))
result = output(data)


