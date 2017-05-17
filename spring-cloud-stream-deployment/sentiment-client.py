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
import requests
import json
from springcloudstream.stream import Processor

url = 'http://sentiment-compute-flask.cfapps.pez.pivotal.io/polarity_compute'


def process(request):
    try:
        response = requests.post(url, data=request, headers={'Content-Type': 'application/json'})
        doc = json.loads(response.text)
        tweets = json.loads(request)
        result = []
        for i, polarity in enumerate(doc['polarity']):
            result.append({'polarity': polarity, 'text': tweets['data'][i]})

        return json.dumps(result)
    except:
        return json.dumps([])


Processor().start(process)
