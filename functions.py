import matplotlib.pyplot as plt
import numpy as np
import textwrap

def cost(y, pred, R, chunk_size=500):
    cost = 0
    for i in range(0, y.shape[0], chunk_size):
        cost += np.sum(
                np.square(
                np.subtract(y[i:i+chunk_size], pred[i:i+chunk_size] * R[i:i+chunk_size])
            )
        )
    return cost/2

def draw_x_gametimes(df):
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.bar([textwrap.fill(game, 10) for game in df.iloc[:, 1]], df.iloc[:, 2])
    ax.set_xlabel('Game')
    ax.set_ylabel('Playtime(log2)')
    ax.set_yscale('log', base=2)
    ax.tick_params(axis='x', labelsize=9)
    plt.show()

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