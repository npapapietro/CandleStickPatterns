import candlestickpatterns
import quandl
from datetime import datetime

t1 = datetime.now().strftime("%Y-%m-%d")
df = quandl.get('BCHARTS/BITSTAMPUSD',start_date = "2015-01-01",end_date=t1)

t=candlestickpatterns.pattern_generate(df)
#candlestickpatterns.candlestick_plot(df,Highlight=t)
