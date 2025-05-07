import crawler_module as m
from time import sleep
import pandas as pd
import matplotlib.pyplot as plt
import talib
import mpl_finance as mpf
all_list=[] #存取所有日期的股市資料
stock_symbol,dates,start_date,end_date=m.get_data()
for date in dates:
    sleep(1) #爬取一筆暫停1秒
    try:
        crawler_data=m.craw_data(date,stock_symbol)
        all_list.append(crawler_data[0])
        df_columns=crawler_data[1]
        print(f'OK! DATE={date},stock symbol={stock_symbol}')
    except Exception as e:
        print('error:',e)
all_df=pd.DataFrame(all_list,columns=df_columns)

#準備資料
day=all_df['日期'].astype(str)
close_price=all_df['收盤價'].astype(float)
open_price=all_df['開盤價'].astype(float)
high_price=all_df['最高價'].astype(float)
low_price=all_df['最低價'].astype(float)
volume=all_df['成交股數'].str.replace(',','').astype(float)
#建立plot物件
fig,(ax,ax2)=plt.subplots(2,1,sharex=True,figsize=(24,15),dpi=100)
ax.set_title(f'{stock_symbol} K線圖({start_date}~{end_date})')

#第一個子圖(K線圖)
mpf.candlestick2_ochl(ax,open_price,close_price,high_price,low_price,width=0.5,colorup='r',colordown='g',alpha=0.6)#繪製蠟燭圖
ax.plot(talib.SMA(close_price,10),label='10日均線')
ax.plot(talib.SMA(close_price,30),label='30日均線')
ax.legend(loc='best',fontsize=20)
ax.grid(True)
#第二個子圖(量能圖)
mpf.volume_overlay(ax2,open_price,close_price,volume,colorup='r',colordown='g',width=0.5,alpha=0.8)#繪製量能圖
ax2.set_xticks(range(0,len(day),5))
ax2.set_xticklabels(day[::5])
ax2.grid(True)
#顯示繪圖
plt.show()