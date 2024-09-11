import matplotlib.pyplot as plt
import textwrap
import numpy as np
import pandas as pd

def draw_history(x, history):
    plt.plot(x, history)
    plt.xlabel('Number of iterations')
    plt.ylabel('Cost')
    plt.show()

def draw_log_history(x,history):
    plt.plot(x, history)
    plt.xlabel('Number of iterations')
    plt.ylabel('Cost\n(log10)')
    plt.yscale('log', base=10)
    plt.show()

def draw_userx_gametimes(df, game_df, theta, I, num_games):
    user = df.sort_values(by='playtime', ascending=False).head(num_games)[['game_id', 'playtime']]
    user_games = game_df.set_index(game_df.game_id).loc[user.game_id, 'game_name']
    user_playtimes = user[['game_id', 'playtime']]
    user_playtimes.playtime = user_playtimes.playtime.div(60)
    actual_top_games = pd.merge(user_games, user_playtimes, on=['game_id'])

    pred = theta @ I.T
    top = np.sort(pred)[-num_games:]
    topi = np.where(np.isin(pred, top))

    time_df = pd.DataFrame({'game_id': np.array(topi).flatten(), 'predicted_playtime': pred[topi].flatten()})
    time_df.predicted_playtime = time_df.predicted_playtime.div(60)
    pred_top_games = pd.merge(game_df.iloc[topi], time_df, on=['game_id'])
    pred_top_games  = pred_top_games.sort_values(ascending=False, by=['predicted_playtime'])
    pred_top_games  = pred_top_games.reset_index(drop=True)

    dfs = [actual_top_games, pred_top_games]

    fig, axs = plt.subplots(2, 1, figsize=(20, 10))
    for i, (ax, df) in enumerate(zip(axs, dfs)):
        ax.bar([textwrap.fill(game, 10) for game in df.iloc[:, 1]], df.iloc[:, 2])
        ax.set_xlabel('Game')
        ax.set_ylabel('Playtime\n(hours)')
        ax.tick_params(axis='x', labelsize=9)

        if i == 0:
            ax.set_title('Actual top games')
        if i == 1:
            ax.set_title('Predicted top games')
    plt.show()