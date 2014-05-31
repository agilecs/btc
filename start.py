from json import loads
from urllib2 import Request, urlopen
def get_last_deal(ticker, nest, last, currency):
    baseurl = 'http://t.btc123.com/m.js'
    req = Request(baseurl + '?type=' + ticker)
    try:
        response = urlopen(req)
        json_str = response.read()
        json_obj = loads(json_str)
        if nest == 'yes':
            return json_obj['ticker'][last] 
        else: 
            return json_obj[last]
    except URLError as e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
    else:
        pass # do nothing

def get_exchangerate(currency):
    cny1usd = 0.1601
    usd1cny = 6.2460
    if currency == 'usd':
        return cny1usd
    else:
        return usd1cny

#bitstamp.net
print get_last_deal(ticker='bitstampTicker', nest='no', last='last', currency='usd')
#btc-e.com
print get_last_deal(ticker='btceBTCUSDticker', nest='yes', last='avg', currency='usd')
#bitfinex.com
print get_last_deal(ticker='bitfinexbtcusdTic', nest='no', last='last_price', currency='usd')
#796.com
print get_last_deal(ticker='796futuresTicker', nest='yes', last='last', currency='usd')
#btcchina.com
print get_last_deal(ticker='btcchinaTicker', nest='yes', last='last', currency='cny')
#huobi.com
print get_last_deal(ticker='huobiTicker', nest='yes', last='last', currency='cny')
#chbtc.com
print get_last_deal(ticker='chbtcTicker', nest='yes', last='last', currency='cny')
#okcoin.com
print get_last_deal(ticker='okcoinTicker', nest='yes', last='last', currency='cny')
#btctrade.com
print get_last_deal(ticker='btctradeTicker', nest='no', last='last', currency='cny')
#btc100.org
print get_last_deal(ticker='btc100Ticker', nest='yes', last='last', currency='cny')
#bter.com
print get_last_deal(ticker='bterTicker', nest='no', last='last', currency='cny')

