from ccxt import binanceusdm
import pandas as pd
from time import sleep
from ta.volatility import average_true_range as atr
from ta.volatility import bollinger_hband as bh
from ta.volatility import bollinger_lband as bl
import numpy as np
import requests
import datetime

np.seterr(all='ignore')

exchange = binanceusdm()


# if you want Telegram alertes edit below code
def cralert(botmesaj, idd=str()):
    return
# def cralert(botmesaj, idd=str('your telegram id here')):
#     bottoken = 'Your bot token here'
#     chat_id = idd
#     url = 'https://api.telegram.org/bot' + bottoken + '/sendMessage?chat_id=' + chat_id + \
#           '&parse_mode=Markdown&text=' + botmesaj
#     requests.get(url)


lst1 = ['RLC/USDT']

clist = ['BTCUSDT', 'ETHUSDT', 'BCHUSDT', 'XRPUSDT', 'EOSUSDT', 'LTCUSDT', 'TRXUSDT', 'ETCUSDT', 'LINKUSDT', 'XLMUSDT',
        'ADAUSDT', 'XMRUSDT', 'DASHUSDT', 'ZECUSDT', 'XTZUSDT', 'BNBUSDT', 'ATOMUSDT', 'ONTUSDT', 'IOTAUSDT', 'BATUSDT',
        'VETUSDT', 'NEOUSDT', 'QTUMUSDT', 'IOSTUSDT', 'THETAUSDT', 'ALGOUSDT', 'ZILUSDT', 'KNCUSDT', 'ZRXUSDT',
        'COMPUSDT', 'OMGUSDT', 'DOGEUSDT', 'SXPUSDT', 'KAVAUSDT', 'BANDUSDT', 'RLCUSDT', 'WAVESUSDT', 'MKRUSDT',
        'SNXUSDT', 'DOTUSDT', 'DEFIUSDT', 'YFIUSDT', 'BALUSDT', 'CRVUSDT', 'TRBUSDT', 'RUNEUSDT', 'SUSHIUSDT',
        'EGLDUSDT', 'SOLUSDT', 'ICXUSDT', 'STORJUSDT', 'BLZUSDT', 'UNIUSDT', 'AVAXUSDT', 'FTMUSDT',
        'ENJUSDT', 'FLMUSDT', 'RENUSDT', 'KSMUSDT', 'NEARUSDT', 'AAVEUSDT', 'FILUSDT', 'RSRUSDT',
        'LRCUSDT', 'MATICUSDT', 'OCEANUSDT', 'BELUSDT', 'AXSUSDT', 'ALPHAUSDT', 'ZENUSDT',
        'SKLUSDT', 'GRTUSDT', '1INCHUSDT', 'CHZUSDT', 'SANDUSDT', 'ANKRUSDT', 'LITUSDT', 'UNFIUSDT',
        'REEFUSDT', 'RVNUSDT', 'SFPUSDT', 'XEMUSDT', 'COTIUSDT', 'CHRUSDT', 'MANAUSDT', 'ALICEUSDT',
        'HBARUSDT', 'ONEUSDT', 'LINAUSDT', 'STMXUSDT', 'DENTUSDT', 'CELRUSDT', 'HOTUSDT', 'MTLUSDT', 'OGNUSDT',
        'NKNUSDT', '1000SHIBUSDT', 'BAKEUSDT', 'GTCUSDT', 'BTCDOMUSDT', 'IOTXUSDT',
        'C98USDT', 'MASKUSDT', 'ATAUSDT', 'DYDXUSDT', '1000XECUSDT', 'GALAUSDT', 'CELOUSDT', 'ARUSDT',
        'KLAYUSDT', 'ARPAUSDT', 'CTSIUSDT', 'LPTUSDT', 'ENSUSDT', 'PEOPLEUSDT', 'ROSEUSDT', 'DUSKUSDT',
        'FLOWUSDT', 'IMXUSDT', 'API3USDT', 'GMTUSDT', 'APEUSDT', 'WOOUSDT', 'JASMYUSDT', 'DARUSDT',
        'GALUSDT', 'OPUSDT', 'INJUSDT', 'STGUSDT', 'SPELLUSDT', '1000LUNCUSDT', 'LUNA2USDT', 'LDOUSDT', 'ICPUSDT',
        'APTUSDT', 'QNTUSDT', 'FETUSDT', 'FXSUSDT', 'HOOKUSDT', 'MAGICUSDT',
        'TUSDT', 'RNDRUSDT', 'HIGHUSDT', 'MINAUSDT', 'ASTRUSDT', 'AGIXUSDT', 'PHBUSDT', 'GMXUSDT', 'CFXUSDT', 'STXUSDT',
        'BNXUSDT', 'ACHUSDT', 'SSVUSDT', 'CKBUSDT', 'PERPUSDT', 'TRUUSDT', 'LQTYUSDT', 'USDCUSDT',
        'IDUSDT', 'ARBUSDT', 'JOEUSDT', 'TLMUSDT', 'AMBUSDT', 'LEVERUSDT', 'RDNTUSDT', 'HFTUSDT', 'XVSUSDT', 'BLURUSDT',
        'EDUUSDT', 'SUIUSDT', '1000PEPEUSDT', '1000FLOKIUSDT', 'UMAUSDT', 'KEYUSDT', 'COMBOUSDT',
        'NMRUSDT', 'MAVUSDT', 'XVGUSDT', 'WLDUSDT', 'PENDLEUSDT', 'ARKMUSDT', 'AGLDUSDT', 'YGGUSDT',
        'DODOXUSDT', 'BNTUSDT', 'OXTUSDT', 'SEIUSDT', 'CYBERUSDT', 'HIFIUSDT', 'ARKUSDT', 'FRONTUSDT',
        'BICOUSDT', 'LOOMUSDT', 'BIGTIMEUSDT', 'BONDUSDT', 'ORBSUSDT', 'STPTUSDT', 'WAXPUSDT', 'BSVUSDT',
        'RIFUSDT', 'POLYXUSDT', 'GASUSDT', 'POWRUSDT', 'TIAUSDT', 'SNTUSDT', 'CAKEUSDT', 'MEMEUSDT',
        'TWTUSDT', 'TOKENUSDT', 'ORDIUSDT', 'STEEMUSDT', 'BADGERUSDT', 'ILVUSDT', 'NTRNUSDT', 'KASUSDT',
        'BEAMXUSDT', '1000BONKUSDT', 'PYTHUSDT', 'SUPERUSDT', 'USTCUSDT', 'ONGUSDT', 'ETHWUSDT', 'JTOUSDT',
        '1000SATSUSDT', 'AUCTIONUSDT', '1000RATSUSDT', 'ACEUSDT', 'MOVRUSDT', 'NFPUSDT', 'BTCUSDT_240628',
        'ETHUSDT_240628', 'AIUSDT', 'XAIUSDT', 'WIFUSDT', 'MANTAUSDT', 'ONDOUSDT', 'LSKUSDT', 'ALTUSDT', 'JUPUSDT',
        'ZETAUSDT', 'RONINUSDT', 'DYMUSDT', 'OMUSDT', 'PIXELUSDT', 'STRKUSDT', 'MAVIAUSDT', 'GLMUSDT', 'PORTALUSDT',
        'TONUSDT', 'AXLUSDT', 'MYROUSDT', 'METISUSDT', 'AEVOUSDT', 'VANRYUSDT', 'BOMEUSDT', 'ETHFIUSDT', 'ENAUSDT',
        'WUSDT', 'TNSRUSDT', 'SAGAUSDT', 'TAOUSDT', 'OMNIUSDT',
        'REZUSDT', 'BBUSDT', 'NOTUSDT']

# Edit here if you want to check on multiple timeframes
timeframes = ['1m', '5m', '15m', '30m', '1h', '4h', '1d']
onetime = ['1m']

current_time = datetime.datetime.now()
ttime = current_time + datetime.timedelta(hours=4)
asdw = ['n']

low0, high0, low1, high1, low2, high2, low3, high3 = 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00

alertes = []
highs = []
lows = []
siralama = ['n']
last_s = []

print("Starting While loop")

# aynı coinde birden fazla farklı alert vermiyor düzeltilecek

while 1:
    for i in clist:
        try:
            for tf in onetime:
                df = exchange.fetch_ohlcv(i, timeframe=tf, limit=802)
                df = pd.DataFrame(df, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
                df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
                df['bhb'] = bh(df['close'])
                df['blb'] = bl(df['close'])
                df['atrr'] = atr(df['high'], df['low'], df['close'])
                t = df['close'][300] / df['atrr'][300]
                # print("Now Checking ", i, tf)

                for s in range(22, len(df.index)):
                    if df['high'][s] > df['bhb'][s]:
                        if siralama[-1] == 'n':
                            highs.append(df['high'][s])
                            siralama.append('h')
                            last_s.append(s)

                        if siralama[-1] == 'h':
                            del highs[-1]
                            highs.append(df['high'][s])
                            siralama.append('h')
                            last_s.append(s)

                        if siralama[-1] == 'l':
                            highs.append(df['high'][s])
                            siralama.append('h')
                            last_s.append(s)

                    if df['low'][s] < df['blb'][s]:
                        if siralama[-1] == 'n':
                            lows.append(df['low'][s])
                            siralama.append('h')
                            last_s.append(s)

                        if siralama[-1] == 'l':
                            del lows[-1]
                            lows.append(df['low'][s])
                            siralama.append('l')
                            last_s.append(s)

                        if siralama[-1] == 'h':
                            lows.append(df['low'][s])
                            siralama.append('l')
                            last_s.append(s)

                high0 = highs[-1]
                high1 = highs[-2]
                high2 = highs[-3]
                high3 = highs[-4]
                low0 = lows[-1]
                low1 = lows[-2]
                low2 = lows[-3]
                low3 = lows[-4]

                # print(i)
                # print(i,  "  price: ", df['close'][301])
                # print("level: ", high0 - ((high0 - low0) * 0.61))
                if siralama[-1] == 'h' and low0 < low1 < high1 < high0:
                    if low0 < df['close'][801] < high0 - ((high0 - low0) * 0.786):
                        if i not in asdw:
                            print("Price in Fibo level try LONG1")
                            print("Timeframe: ", tf)

                            cralert(f"{i} - {tf} REALTIME --- Fibo level try LONG\n T:{t}")
                            asdw.append(i)
                            alertes.append(5)
                        else:
                            if 5 not in alertes:
                                cralert(f"{i} - {tf} REALTIME --- Fibo level try LONG\n T:{t}")
                                alertes.append(5)
                            if datetime.datetime.now() > ttime:
                                asdw.clear()
                                ttime = datetime.datetime.now() + datetime.timedelta(hours=4)
                                alertes.clear()

                if siralama[-1] == 'l' and low1 < low2 < high1 < high0:
                    if low1 < df['close'][801] < high0 - ((high0 - low1) * 0.786):
                        print("Price in Fibo level try LONG")
                        if i not in asdw:
                            print("Price in Fibo level try LONG2")
                            print("Timeframe: ", tf)

                            cralert(f"{i} - {tf} REALTIME --- Fibo level try LONG\n T:{t}")
                            asdw.append(i)
                            alertes.append(5)
                        else:
                            if 5 not in alertes:
                                cralert(f"{i} - {tf} REALTIME --- Fibo level try LONG\n T:{t}")
                                alertes.append(5)
                            if datetime.datetime.now() > ttime:
                                asdw.clear()
                                ttime = datetime.datetime.now() + datetime.timedelta(hours=4)
                                alertes.clear()

                if siralama[-1] == 'l' and low0 < low1 < high1 < high0:
                    if high0 > df['close'][801] > low0 + ((high0 - low0) * 0.786):
                        if i not in asdw:
                            print("Price in Fibo level try SHORT1")
                            print("Timeframe: ", tf)

                            cralert(f"{i} - {tf} REALTIME --- Fibo level try SHORT\n T:{t}")
                            asdw.append(i)
                            alertes.append(6)
                        else:
                            if 6 not in alertes:
                                cralert(f"{i} - {tf} REALTIME --- Fibo level try SHORT\n T:{t}")
                                alertes.append(6)
                            if datetime.datetime.now() > ttime:
                                asdw.clear()
                                ttime = datetime.datetime.now() + datetime.timedelta(hours=4)
                                alertes.clear()

                if siralama[-1] == 'h' and low0 < low1 < high2 < high1:
                    if high1 > df['close'][801] > low0 + ((high1 - low0) * 0.786):
                        if i not in asdw:
                            print("Price in Fibo level try SHORT2")
                            print("Timeframe: ", tf)

                            cralert(f"{i} - {tf} REALTIME --- Fibo level try SHORT\n T:{t}")
                            asdw.append(i)
                            alertes.append(6)
                        else:
                            if 6 not in alertes:
                                cralert(f"{i} - {tf} REALTIME --- Fibo level try SHORT\n T:{t}")
                                alertes.append(6)
                            if datetime.datetime.now() > ttime:
                                asdw.clear()
                                ttime = datetime.datetime.now() + datetime.timedelta(hours=4)
                                alertes.clear()

                if low0 > high0 and siralama[-1] == 'h' and (last_s[-1] == 800 or last_s[-1] == 799):
                    if i not in asdw:
                        print(i, " REALTIME --- Extreme Down Trend")
                        print("Timeframe: ", tf)

                        cralert(f"{i} - {tf} REALTIME --- Extreme Down Trend\n T:{t}")
                        asdw.append(i)
                        alertes.append(1)
                    else:
                        if 1 not in alertes:
                            cralert(f"{i} - {tf} REALTIME --- Extreme Down Trend\n T:{t}")
                            alertes.append(1)
                        if datetime.datetime.now() > ttime:
                            asdw.clear()
                            ttime = datetime.datetime.now() + datetime.timedelta(hours=4)
                            alertes.clear()

                if low0 > high0 and siralama[-1] == 'l' and (last_s[-1] == 800 or last_s[-1] == 799):
                    if i not in asdw:
                        print(i, " REALTIME --- Extreme Up Trend")
                        print("Timeframe: ", tf)

                        cralert(f"{i} - {tf} REALTIME --- Extreme Up Trend\n T:{t}")
                        asdw.append(i)
                        alertes.append(2)
                    else:
                        if 2 not in alertes:
                            cralert(f"{i} - {tf} REALTIME --- Extreme Up Trend\n T:{t}")
                            alertes.append(1)
                        if datetime.datetime.now() > ttime:
                            asdw.clear()
                            ttime = datetime.datetime.now() + datetime.timedelta(hours=4)
                            alertes.clear()

                # Change in market direction Choch, not only choch, but it only alerts when best time to sell
                if high1 > high0 > high2 > low2 < low1 > low0 and siralama[-1] == 'h' and (
                        last_s[-1] == 300 or last_s[-1] == 299):
                    if i not in asdw:
                        print(i, " REALTIME --- Choch from uptrend to DownTrend now good to SHORT")
                        print("Timeframe: ", tf)

                        cralert(f"{i} - {tf} REALTIME --- Choch from uptrend to DownTrend now good to SHORT\n T:{t}")
                        asdw.append(i)
                        alertes.append(3)
                    else:
                        if 3 not in alertes:
                            cralert(
                                f"{i} - {tf} REALTIME --- Choch from uptrend to DownTrend now good to SHORT\n T:{t}")
                            alertes.append(3)
                        if datetime.datetime.now() > ttime:
                            asdw.clear()
                            ttime = datetime.datetime.now() + datetime.timedelta(hours=4)
                            alertes.clear()

                if low1 < low0 < low2 < high2 > high1 < high0 and siralama[-1] == 'l' and (
                        last_s[-1] == 300 or last_s[-1] == 299):
                    if i not in asdw:
                        print(i, " REALTIME --- Choch from downtrend to UpTrend now good to LONG")
                        print("Timeframe: ", tf)

                        cralert(f"{i} - {tf} REALTIME --- Choch from downtrend to UpTrend now good to LONG\n T:{t}")
                        asdw.append(i)
                        alertes.append(4)
                    else:
                        if 4 not in alertes:
                            cralert(f"{i} - {tf} REALTIME --- Choch from downtrend to UpTrend now good to LONG\n T:{t}")
                            alertes.append(4)
                        if datetime.datetime.now() > ttime:
                            asdw.clear()
                            ttime = datetime.datetime.now() + datetime.timedelta(hours=4)
                            alertes.clear()

                # Normal Long opportunity in UpTrend
                if low1 < low0 < high1 < high0 and siralama[-1] == 'l' and (last_s[-1] == 300 or last_s[-1] == 299):
                    if i not in asdw:
                        print(i, " REALTIME --- Up Trend Good to Long")
                        print("Timeframe: ", tf)

                        cralert(f"{i} - {tf} REALTIME --- Up Trend Good to Long\n T:{t}")
                        asdw.append(i)
                        alertes.append(5)
                    else:
                        if 5 not in alertes:
                            cralert(f"{i} - {tf} REALTIME --- Up Trend Good to Long\n T:{t}")
                            alertes.append(5)
                        if datetime.datetime.now() > ttime:
                            asdw.clear()
                            ttime = datetime.datetime.now() + datetime.timedelta(hours=4)
                            alertes.clear()

                # Normal Short opportunity in DownTrend
                if high1 > high0 > low1 > low0 and siralama[-1] == 'h' and (last_s[-1] == 300 or last_s[-1] == 299):
                    if i not in asdw:
                        print(i, " REALTIME --- Down Trend Good to Short")
                        print("Timeframe: ", tf)

                        cralert(f"{i} - {tf} REALTIME --- Down Trend Good to Short\n T:{t}")
                        asdw.append(i)
                        alertes.append(6)
                    else:
                        if 6 not in alertes:
                            cralert(f"{i} - {tf} REALTIME --- Down Trend Good to Short\n T:{t}")
                            alertes.append(6)
                        if datetime.datetime.now() > ttime:
                            asdw.clear()
                            ttime = datetime.datetime.now() + datetime.timedelta(hours=4)
                            alertes.clear()

                highs.clear()
                lows.clear()
                siralama.clear()
                siralama = ['n']
                sleep(0.3)
                last_s.clear()

        except Exception as x:
            print("The error is: ", x)
            continue
