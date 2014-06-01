from datetime import datetime
from json import loads
from urllib2 import Request, urlopen
def get_last_deal(ticker, nest, last):
    print ' >>> getting data from ' + ticker + ' ... ... '
    baseurl = 'http://t.btc123.com/m.js'
    req = Request(baseurl + '?type=' + ticker)
    try:
        response = urlopen(req)
        json_str = response.read()
        json_obj = loads(json_str)
        if nest == 'yes':
            last_str = json_obj['ticker'][last] 
            return float('%.2f' % float(last_str))
        else: 
            last_str = json_obj[last]
            return float('%.2f' % float(last_str))
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

def usd2cny(usd):
    return float('%.2f' % (get_exchangerate('cny') * usd))

def cny2usd(cny):
    return float('%.2f' % (get_exchangerate('usd') * cny))

def del_large_small_and_avg(list_as_stack):
    list_as_stack.sort()
    list_as_stack.pop()
    list_as_stack.reverse()
    list_as_stack.pop()
    avg = sum(list_as_stack) / 9
    return avg

def get_usd_cny():
    usd_stack = []
    cny_stack = []
    #bitstamp.net
    bitstamp_usd = get_last_deal('bitstampTicker', 'no', 'last')
    bitstamp_cny = usd2cny(bitstamp_usd)
    usd_stack.append(bitstamp_usd)
    cny_stack.append(bitstamp_cny)
    #btc-e.com
    btc_e_usd = get_last_deal('btceBTCUSDticker', 'yes', 'avg')
    btc_e_cny = usd2cny(btc_e_usd)
    usd_stack.append(btc_e_usd)
    cny_stack.append(btc_e_cny)
    #bitfinex.com
    bitfinex_usd = get_last_deal('bitfinexbtcusdTic', 'no', 'last_price')
    bitfinex_cny = usd2cny(bitfinex_usd)
    usd_stack.append(bitfinex_usd)
    cny_stack.append(bitfinex_cny)
    #796.com
    _796_usd = get_last_deal('796futuresTicker', 'yes', 'last')
    _796_cny = usd2cny(_796_usd)
    usd_stack.append(_796_usd)
    cny_stack.append(_796_cny)
    #btcchina.com
    btcchina_cny = get_last_deal('btcchinaTicker', 'yes', 'last')
    btcchina_usd = cny2usd(btcchina_cny)
    cny_stack.append(btcchina_cny)
    usd_stack.append(btcchina_usd)
    #huobi.com
    huobi_cny = get_last_deal('huobiTicker', 'yes', 'last')
    huobi_usd = cny2usd(huobi_cny)
    cny_stack.append(huobi_cny)
    usd_stack.append(huobi_usd)
    #chbtc.com
    chbtc_cny = get_last_deal('chbtcTicker', 'yes', 'last')
    chbtc_usd = cny2usd(chbtc_cny)
    cny_stack.append(chbtc_cny)
    usd_stack.append(chbtc_usd)
    #okcoin.com
    okcoin_cny = get_last_deal('okcoinTicker', 'yes', 'last')
    okcoin_usd = cny2usd(okcoin_cny)
    cny_stack.append(okcoin_cny)
    usd_stack.append(okcoin_usd)
    #btctrade.com
    btctrade_cny = get_last_deal('btctradeTicker', 'no', 'last')
    btctrade_usd = cny2usd(btctrade_cny)
    cny_stack.append(btctrade_cny)
    usd_stack.append(btctrade_usd)
    #btc100.org
    btc100_cny = get_last_deal('btc100Ticker', 'yes', 'last')
    btc100_usd = cny2usd(btc100_cny)
    cny_stack.append(btc100_cny)
    usd_stack.append(btc100_usd)
    #bter.com
    bter_cny = get_last_deal('bterTicker', 'no', 'last')
    bter_usd = cny2usd(bter_cny)
    cny_stack.append(bter_cny)
    usd_stack.append(bter_usd)

    usd_avg = del_large_small_and_avg(usd_stack)
    cny_avg = del_large_small_and_avg(cny_stack)
    
    usd_cny = []
    usd_cny.append(float('%.2f' % usd_avg))
    usd_cny.append(float('%.2f' % cny_avg))
    return usd_cny

def generate_csv_file():
    csv_file = open('btc.csv', 'a')
    now = datetime.now()
    time = now.strftime("%y%m%d %H%M")
    usd_cny = get_usd_cny()
    cny = str(usd_cny.pop())
    usd = str(usd_cny.pop())
    csv_file.write(time + ", " + usd + ", " + cny + "\n")
    csv_file.close()
    print ' >>> got the latest value: added into btc.csv'
    print ' <<< ' + time + ', ' + usd + ', ' + cny + '\n'

generate_csv_file()
