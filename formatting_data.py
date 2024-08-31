import pandas as pd
from sklearn.preprocessing import LabelEncoder

def get_data_frame():
    df = pd.read_csv("data\processed\processed_users_items.csv")

    df = df.drop(columns=['index','playtime_2weeks'])

    df = df.rename(columns={'item_id': 'game_id', 'playtime_forever': 'playtime'})

    user_encoder = LabelEncoder()
    games_encoder = LabelEncoder()

    df['user_id'] = user_encoder.fit_transform(df['user_id'])
    df['game_id'] = games_encoder.fit_transform(df['game_id'])

    df['playtime'].quantile(0.55)

    alpha = 61.0 #The 55% quartile will be 0.5
    df['playtime'] = df['playtime'].apply(lambda x: 1 - (1 / (1 + (x / alpha))))

    return df