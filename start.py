from urllib2 import Request, urlopen
req = Request('http://t.btc123.com/m.js?type=bitstampTicker')
try:
    response = urlopen(req)
    html = response.read()
    print html
except URLError as e:
    if hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
    elif hasattr(e, 'code'):
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
else:
    # everything is fine
    print "\n"
