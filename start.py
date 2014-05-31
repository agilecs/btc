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
print '%.2f' % float(get_last_deal('bitstampTicker', 'no', 'last', 'usd'))
#btc-e.com
print '%.2f' % float(get_last_deal('btceBTCUSDticker', 'yes', 'avg', 'usd'))
#bitfinex.com
print '%.2f' % float(get_last_deal('bitfinexbtcusdTic', 'no', 'last_price', 'usd'))
#796.com
print '%.2f' % float(get_last_deal('796futuresTicker', 'yes', 'last', 'usd'))
#btcchina.com
print '%.2f' % (get_exchangerate('usd') * float(get_last_deal('btcchinaTicker', 'yes', 'last', 'cny')))
#huobi.com
print '%.2f' % (get_exchangerate('usd') * float(get_last_deal('huobiTicker', 'yes', 'last', 'cny')))
#chbtc.com
print '%.2f' % (get_exchangerate('usd') * float(get_last_deal('chbtcTicker', 'yes', 'last', 'cny')))
#okcoin.com
print '%.2f' % (get_exchangerate('usd') * float(get_last_deal('okcoinTicker', 'yes', 'last', 'cny')))
#btctrade.com
print '%.2f' % (get_exchangerate('usd') * float(get_last_deal('btctradeTicker', 'no', 'last', 'cny')))
#btc100.org
print '%.2f' % (get_exchangerate('usd') * float(get_last_deal('btc100Ticker', 'yes', 'last', 'cny')))
#bter.com
print '%.2f' % (get_exchangerate('usd') * float(get_last_deal('bterTicker', 'no', 'last', 'cny')))
