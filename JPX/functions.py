import pandas as pd
import time
import datetime

#経過時間をprint出力する関数
#引数：基準時間(time型)
def el_time(s_time):
    e_time = time.time()
    timedelta = round(e_time - s_time,0)
    print(timedelta)
    


#銘柄毎のデータフレームを持つ辞書の、特定のカラムの時系列データを抽出し新たなデータフレームを作成
#引数：colum　抽出したいカラム名 b_dict：銘柄毎のデータフレームが格納された辞書

#例）辞書｛銘柄：データフレーム（index：日付、column：始値、終値、…、シャープ値）｝
#　　→　新しいデータフレーム（index：日付、columns：銘柄、値：シャープ値）

def brand_ts(b_dict,colum):
    new_list = ['Date']
    new_df = pd.DataFrame()
    count= 0

    #処理に時間がかかるので、途中経過を表示
    s_time = time.time()
    
    #辞書から銘柄毎の特徴量を抽出し、新たなリストを作成
    for k,v in b_dict.items():
        new_list.append(k)
        df_tmp = v[['Date',colum]]
        if count!=0:
            new_df = pd.merge(new_df,df_tmp,on='Date',how='outer')
        else:
            new_df = df_tmp
        count+=1
        
        if count%100 ==0:
            el_time(s_time)
    
    new_df.fillna(0,inplace=True)
    new_df.columns = new_list
    return new_df