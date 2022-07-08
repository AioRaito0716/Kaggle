import pandas as pd

log = pd.read_table('gnss_log.txt',header=20)

log.head(10)

log_df =log['# '].str.split(',',expand=True)

name = log_df[0].unique()

df_dict = {}
for sta in name:
    df_dict[sta] = log_df[log_df[0]==sta]

#Rawのカラム情報
cols = pd.read_table('gnss_log.txt',header=4,nrows=1)

col_raw = list(cols['# '].str.split(','))

df_dict['Raw'].columns = col_raw
df_dict['Raw'].drop('# Raw',axis=1,inplace=True)

df_dict.keys()

#UncalAccelのカラム情報
cols_acc = pd.read_table('gnss_log.txt',header=6,nrows=1)

col_acc = cols_acc['# '].str.split(',')

name1 = 'UncalAccel'
df_dict[name1].drop(df_dict[name1].columns[len(col_acc[0]):],axis=1,inplace=True)
df_dict[name1].columns = col_acc[0]
df_dict[name1].drop('# {}'.format(name1),axis=1,inplace=True)

df_dict['UncalAccel']

#UncalGyroのカラム情報
cols_gyr = pd.read_table('gnss_log.txt',header=8,nrows=1)

col_gyr = cols_gyr['# '].str.split(',')

name2 = 'UncalGyro'
df_dict[name2].drop(df_dict[name2].columns[len(col_gyr[0]):],axis=1,inplace=True)
df_dict[name2].columns = col_gyr[0]
df_dict[name2].drop('# {}'.format(name2),axis=1,inplace=True)

df_dict['UncalGyro']

#UncalMagのカラム情報
cols_mag = pd.read_table('gnss_log.txt',header=10,nrows=1)

col_mag = cols_mag['# '].str.split(',')

name3 = 'UncalMag'
df_dict[name3].drop(df_dict[name3].columns[len(col_mag[0]):],axis=1,inplace=True)
df_dict[name3].columns = col_mag[0]
df_dict[name3].drop('# {}'.format(name3),axis=1,inplace=True)

df_dict['UncalMag']