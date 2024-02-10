import vectorbt as vbt

btc_price =  vbt.YFData.download(
        'BTC-USD',
        missing_index='drop').get('Close')

#print(btc_price)
#print(type(btc_price))

# create RSI indicator ()
rsi = vbt.RSI.run(btc_price, window=14)
#print(rsi.rsi)

# define strategy entries and exits
entries = rsi.rsi_crossed_below(30)
exits = rsi.rsi_crossed_above(70)
#print(str(entries))

# run strategy backtest
pf =  vbt.Portfolio.from_signals(btc_price, entries, exits)

# show backtest results as stats
#print(pf.stats())

# show single stats like total return
#print(pf.total_return())

# a basic plot
pf.plot().show()