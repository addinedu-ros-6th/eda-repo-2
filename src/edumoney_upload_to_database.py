#%%
import pandas as pd
import mysql.connector


#%%
df = pd.read_csv("../data/edumoney_data/서울경기2013_2022예산.csv", encoding='utf-8')

df = pd.DataFrame(df)

#%%
df.head()
df.drop(['Unnamed: 0'],axis=1, inplace=True)
df.head()
#%%
df.info()
#%%
remote = mysql.connector.connect(
    host = '',
    user = '',
    password = '',
    database = ''
)


#%%
cur = remote.cursor(buffered=True)

#%%
sql="""create table education_money(
            city varchar(32),
            year int,
            0_19 int,
            20_100 int,
            예산 float
            );"""
cur.execute(sql)
remote.commit()

#%%
sql="""insert into education_money Values (%s,%s,%s,%s,%s);"""

for i , row in df.iterrows():
    cur.execute(sql,tuple(row))
    # print(tuple(row))
    remote.commit()

#%%
remote.close()

# %%
