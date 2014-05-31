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

def get_avg():
    usd_stack = []
    cny_stack = []
    #bitstamp.net
    bitstamp = get_last_deal('bitstampTicker', 'no', 'last', 'usd')
    bitstamp_cny = float('%.2f' % (get_exchangerate('cny') * float(bitstamp)))
    bitstamp_usd = float('%.2f' % float(bitstamp))
    usd_stack.append(bitstamp_usd)
    cny_stack.append(bitstamp_cny)
    #btc-e.com
    btc_e = get_last_deal('btceBTCUSDticker', 'yes', 'avg', 'usd')
    btc_e_cny = float('%.2f' % (get_exchangerate('cny') * float(btc_e)))
    btc_e_usd = float('%.2f' % float(btc_e))
    usd_stack.append(btc_e_usd)
    cny_stack.append(btc_e_cny)
    #bitfinex.com
    bitfinex = get_last_deal('bitfinexbtcusdTic', 'no', 'last_price', 'usd')
    bitfinex_cny = float('%.2f' % (get_exchangerate('cny') * float(bitfinex)))
    bitfinex_usd = float('%.2f' % float(bitfinex))
    usd_stack.append(bitfinex_usd)
    cny_stack.append(bitfinex_cny)
    #796.com
    _796 = get_last_deal('796futuresTicker', 'yes', 'last', 'usd')
    _796_cny = float('%.2f' % (get_exchangerate('cny') * float(_796)))
    _796_usd = float('%.2f' % float(_796))
    usd_stack.append(_796_usd)
    cny_stack.append(_796_cny)
    #btcchina.com
    btcchina = get_last_deal('btcchinaTicker', 'yes', 'last', 'cny')
    btcchina_usd = float('%.2f' % (get_exchangerate('usd') * float(btcchina)))
    btcchina_cny = float('%.2f' % float(btcchina))
    cny_stack.append(btcchina_cny)
    usd_stack.append(btcchina_usd)
    #huobi.com
    huobi = get_last_deal('huobiTicker', 'yes', 'last', 'cny')
    huobi_usd = float('%.2f' % (get_exchangerate('usd') * float(huobi)))
    huobi_cny = float('%.2f' % float(huobi))
    cny_stack.append(huobi_cny)
    usd_stack.append(huobi_usd)
    #chbtc.com
    chbtc = get_last_deal('chbtcTicker', 'yes', 'last', 'cny')
    chbtc_usd = float('%.2f' % (get_exchangerate('usd') * float(chbtc)))
    chbtc_cny = float('%.2f' % float(chbtc))
    cny_stack.append(chbtc_cny)
    usd_stack.append(chbtc_usd)
    #okcoin.com
    okcoin = get_last_deal('okcoinTicker', 'yes', 'last', 'cny')
    okcoin_usd = float('%.2f' % (get_exchangerate('usd') * float(okcoin)))
    okcoin_cny = float('%.2f' % float(okcoin))
    cny_stack.append(okcoin_cny)
    usd_stack.append(okcoin_usd)
    #btctrade.com
    btctrade = get_last_deal('btctradeTicker', 'no', 'last', 'cny')
    btctrade_usd = float('%.2f' % (get_exchangerate('usd') * float(btctrade)))
    btctrade_cny = float('%.2f' % float(btctrade))
    cny_stack.append(btctrade_cny)
    usd_stack.append(btctrade_usd)
    #btc100.org
    btc100 = get_last_deal('btc100Ticker', 'yes', 'last', 'cny')
    btc100_usd = float('%.2f' % (get_exchangerate('usd') * float(btc100)))
    btc100_cny = float('%.2f' % float(btc100))
    cny_stack.append(btc100_cny)
    usd_stack.append(btc100_usd)
    #bter.com
    bter = get_last_deal('bterTicker', 'no', 'last', 'cny')
    bter_usd = float('%.2f' % (get_exchangerate('usd') * float(bter)))
    bter_cny = float('%.2f' % float(bter))
    cny_stack.append(bter_cny)
    usd_stack.append(bter_usd)

    usd_stack.sort()
    usd_stack.pop()
    usd_stack.reverse()
    usd_stack.pop()
    usd_avg = sum(usd_stack) / 9

    cny_stack.sort()
    cny_stack.pop()
    cny_stack.reverse()
    cny_stack.pop()
    cny_avg = sum(cny_stack) / 9
    
    both_avg = []
    both_avg.append(float('%.2f' % usd_avg))
    both_avg.append(float('%.2f' % cny_avg))
    return both_avg

print get_avg()
