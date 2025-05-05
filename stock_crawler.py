import crawler_module as m
from time import sleep
import pandas as pd
import matplotlib.pyplot as plt
all_list=[] #存取所有日期的股市資料
stock_symbol,dates=m.get_data()
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
# price_as_float=all_df['收盤價'].replace(',','')
price=all_df['收盤價'].astype(str)

#建立plot物件
plt.figure(figsize=(20,10),dpi=100)#建立新圖形

#進行繪圖
plt.plot(day,price,'s-',color='r',label='Close Price')#在設定好的圖形上進行繪圖
plt.title("TSMC Line Chart")#設定圖形標題
plt.xticks(fontsize=10,rotation=45)#設定X軸刻度標籤
plt.yticks(fontsize=10)#設定Y軸刻度標籤
plt.legend(loc="best",fontsize=20)#設定圖例

#顯示繪圖
plt.show()