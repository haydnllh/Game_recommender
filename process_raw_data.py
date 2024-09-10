import ast
import pandas as pd

dict_list = []
for line in open('data\\raw\\australian_users_items.json', encoding='utf-8'):
  try:
    k = ast.literal_eval(line)
    dict_list.append(k)
  except:
    continue

df = pd.DataFrame.from_records(dict_list)

frames = []
user_ids = []
count = 0
for index, rows in df.iterrows():
    count += 1
    user_ids.append(rows['user_id'])
    frames.append(pd.json_normalize(rows['items']))
    
df1 = pd.concat(frames, keys=user_ids)

df1.to_csv('data/processed/processed_users_items.csv')