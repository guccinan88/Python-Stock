import crawler_module as m
from time import sleep
import pandas as pd

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
print(all_df.to_string(index=False))