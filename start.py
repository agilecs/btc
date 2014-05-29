from urllib2 import Request, urlopen
import json
baseurl = 'http://t.btc123.com/m.js'
def get_full_json(baseurl, ticker):
    req = Request(baseurl + '?type=' + ticker)
    try:
        response = urlopen(req)
        json_str = response.read()
        return json_str 
    except URLError as e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
    else:
        # everything is fine
        pass # do nothing

bitstampTicker_str = get_full_json(baseurl, ticker='bitstampTicker')
bitstampTicker_obj = json.loads(bitstampTicker_str)
print bitstampTicker_obj['last']
