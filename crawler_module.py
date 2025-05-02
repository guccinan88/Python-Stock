from io import StringIO
import requests
import pandas as pd
from datetime import datetime,timedelta

#讀取設定檔
def get_setting():
    res=[]
    try:
        with open('stock.txt') as f:
            slist=f.readlines()
            print(f'read:{slist}')
            a,b,c=slist[0].split(',')
            res=[a,b,c]
    except:
        print('stock.txt讀取錯誤')
    return res

#篩選工作日
def get_data():
    data=get_setting()
    dates=[]
    start_date=datetime.strptime(data[1],'%Y%m%d')
    end_date=datetime.strptime(data[2],'%Y%m%d')
    for day_number in range((end_date - start_date).days+1):
        date=(start_date+timedelta(days=day_number))
        if date.weekday()<5:
            dates.append(date.strftime('%Y%m%d'))
    return data[0],dates

#爬蟲程式，用來抓取一組日期的股市資料
def craw_data(date,symbol):
    r=requests.get(f'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date={date}&type=ALL',verify=False)
    r_text=[i for i in r.text.split('\n') if len(i.split('",'))==17 and i[0] != '=']
    df=pd.read_csv(StringIO("\n".join(r_text)),header=0)
    df=df.drop(columns=['Unnamed: 16'])
    filter_df=df[df["證券代號"]==symbol]
    filter_df.insert(0,"日期",date)
    return list(filter_df.iloc[0]),filter_df.columns