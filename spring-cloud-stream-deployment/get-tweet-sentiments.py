#!/usr/bin/env jython
"""
Copyright 2017 the original author or authors.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
__author__ = 'David Turanski'

import json
import java.util.Arrays
import java.util.ArrayList

if __name__ == '__main__':
    class Processor:
        def sendAndReceive(self, request):
            data = [{"polarity": 0.8914353672886375,
                     "text": "RT @theBurgans: Wow! I just entered for a chance to win \"Honor &amp; Privilege (Cargon Trilogy Bo...\" by Kimberly Gould (A.... https://t.co/ygM"},
                    {"polarity": 0.9914103188100896,
                     "text": " Happy birthday @that70sgirI and @Mackenziewells_ ! Have an amazing birthday fellow scammers"},
                    {"polarity": 0.767706750644645,
                     "text": "RT @barbiefobia: jimin taking care of a sleeping jungkook despite being tired too; tell me about an angel, bro\n\nI vote for @BTS_twt "}]
            return json.dumps(data)


    processor = Processor()

    with open('./list-of-tweets.txt', 'r') as tweets:
        list = []
        data = json.loads(tweets.read())
        for tweet in data:
            list.append(json.dumps(tweet))
        payload = java.util.ArrayList(java.util.Arrays.asList(list))


####

## Payload is java.util.ArrayList
def input(payload):
    for item in payload:
        tweet = json.loads(item)
        text = []
        if tweet['lang'] == 'en':
            val = tweet['text'].encode('ascii', 'ignore')
            text.append(val)
    result = json.JSONEncoder().encode({"data": text})
    return result


# convert array of dict to array of str to java.util.ArrayList
def output(payload):
    if (payload):
        items = []
        data = json.loads(payload)
        for item in data:
            items.append(json.dumps(item).encode('ascii', 'ignore'))

        return java.util.ArrayList(java.util.Arrays.asList(items))
    return None


data = processor.sendAndReceive(input(payload))
tmp = output(data)
result = tmp

