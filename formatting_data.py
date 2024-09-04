import pandas as pd
from sklearn.preprocessing import LabelEncoder

def get_data_frame():
    df = pd.read_csv("data\processed\processed_users_items.csv")

    df = df.drop(columns=['index','playtime_2weeks'])

    df = df.rename(columns={'item_id': 'game_id', 'playtime_forever': 'playtime', 'item_name': 'game_name'})

    user_encoder = LabelEncoder()
    games_encoder = LabelEncoder()

    df.user_id = user_encoder.fit_transform(df.user_id)
    df.game_id = games_encoder.fit_transform(df.game_id)

    alpha = 61.0 #The 55% quartile will be 0.5
    df.playtime = df.playtime.apply(lambda x: 1 - (1 / (1 + (x / alpha))))

    game_df = df[['game_id', 'game_name']].copy()
    game_df = game_df.drop_duplicates(subset=['game_id'])

    df = df.drop(columns='game_name')

    df = df.sort_values(by=['user_id', 'game_id'])
    game_df = game_df.sort_values(by=['game_id'])

    df = df.reset_index(drop=True)
    game_df = game_df.reset_index(drop=True)

    return df, game_df