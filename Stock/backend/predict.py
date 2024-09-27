import sys
import warnings
import argparse
if not sys.warnoptions:
    warnings.simplefilter('ignore')

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import mpld3
import seaborn as sns
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime, timedelta
from tqdm import tqdm
import os

import yfinance as yf

sns.set()
tf.random.set_seed(1234)

num_layers = 1
size_layer = 64  # Reduced layer size
timestamp = 10
epoch = 100  # Reduced epochs
dropout_rate = 0.3  # Adjusted dropout rate
test_size = 30
learning_rate = 0.01

def predict_stock(symbol, period, sim, future):
    simulation_size = sim
    test_size = future
    
    # Download and prepare data
    df = yf.download(symbol, period=period, interval="1d")
    minmax = MinMaxScaler().fit(df[['Close']].astype('float32'))
    df_log = minmax.transform(df[['Close']].astype('float32'))
    df_log = pd.DataFrame(df_log)
    
    class Model:
        def __init__(self, learning_rate, num_layers, size_layer, output_size, dropout_rate=0.1):
            self.size_layer = size_layer
            self.num_layers = num_layers
            self.output_size = output_size
            self.model = self.build_model(learning_rate, dropout_rate)

        def build_model(self, learning_rate, dropout_rate):
            model = tf.keras.Sequential()
            model.add(tf.keras.layers.Input(shape=(None, self.size_layer)))
            for _ in range(self.num_layers):
                model.add(tf.keras.layers.LSTM(self.size_layer, return_sequences=True, dropout=dropout_rate))
            model.add(tf.keras.layers.LSTM(self.size_layer))
            model.add(tf.keras.layers.Dense(self.output_size))
            model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate), loss='mean_squared_error')
            return model

    def calculate_accuracy(real, predict):
        real = np.array(real) + 1
        predict = np.array(predict) + 1
        percentage = 1 - np.sqrt(np.mean(np.square((real - predict) / real)))
        return percentage * 100

    def anchor(signal, weight):
        buffer = []
        last = signal[0]
        for i in signal:
            smoothed_val = last * weight + (1 - weight) * i
            buffer.append(smoothed_val)
            last = smoothed_val
        return buffer

    def forecast():
        modelnn = Model(
            learning_rate, num_layers, size_layer, df_log.shape[1], dropout_rate
        )
        date_ori = pd.to_datetime(df.index).tolist()

        # Training with smaller batches
        pbar = tqdm(range(0, df_log.shape[0] - timestamp, timestamp), desc='Train Loop')
        for i in pbar:
            batch_end = min(i + timestamp, df_log.shape[0] - timestamp)
            batch_x = np.expand_dims(df_log.iloc[i: batch_end, :].values, axis=0)
            batch_y = df_log.iloc[i + 1: batch_end + 1, :].values
            loss = modelnn.model.train_on_batch(batch_x, batch_y)
            pbar.set_postfix(cost=loss)

        # Predict in batch
        batch_x = np.expand_dims(df_log.values, axis=0)
        output_predict = modelnn.model.predict(batch_x)
        output_predict = np.concatenate((df_log.values, output_predict), axis=0)
        output_predict = minmax.inverse_transform(output_predict)
        deep_future = anchor(output_predict[:, 0], 0.4)

        return deep_future

    results = [forecast() for _ in range(simulation_size)]

    date_ori = pd.to_datetime(df.index).tolist()
    for i in range(test_size):
        date_ori.append(date_ori[-1] + timedelta(days=1))
    date_ori = pd.Series(date_ori).dt.strftime(date_format='%Y-%m-%d').tolist()

    accepted_results = []
    for r in results:
        if (np.array(r[-test_size:]) < np.min(df['Close'])).sum() == 0 and \
        (np.array(r[-test_size:]) > np.max(df['Close']) * 2).sum() == 0:
            accepted_results.append(r)

    accuracies = [calculate_accuracy(df['Close'].values, r[:-test_size]) for r in accepted_results]

    plt.figure(figsize=(11, 5))
    for no, r in enumerate(accepted_results):
        labels = [f"""
        <table style="border: 1px solid black; font-weight:bold; font-size:larger; background-color:white">
        <tr style="border: 1px solid black;">
        <th style="border: 1px solid black;">Date:</th>
        <td style="border: 1px solid black;">{x}</td>
        </tr>
        <tr style="border: 1px solid black;">
        <th style="border: 1px solid black;">Close:</th>
        <td style="border: 1px solid black;">{round(y,2)}</td>
        </tr>
        </table>
        """ for x, y in zip(date_ori[::5], r[::5])]
        lines = plt.plot(date_ori[::5], r[::5], label='Forecast %d' % (no + 1), marker="*")
        tooltips = mpld3.plugins.PointHTMLTooltip(lines[0], labels=labels, voffset=10, hoffset=10)
        mpld3.plugins.connect(plt.gcf(), tooltips)
    lines = plt.plot(df.index.tolist()[::5], df['Close'][::5], label='True Trend', c='black', marker="*")
    labels = [f"""
        <table style="border: 1px solid black; font-weight:bold; font-size:larger; background-color:white">
        <tr style="border: 1px solid black;">
        <th style="border: 1px solid black;">Date:</th>
        <td style="border: 1px solid black;">{y}</td>
        </tr>
        <tr style="border: 1px solid black;">
        <th style="border: 1px solid black;">Close:</th>
        <td style="border: 1px solid black;">{round(x,2)}</td>
        </tr>
    </table>
    """ for x, y in zip(df['Close'].tolist()[::5], df.index.tolist()[::5])]
    tooltips = mpld3.plugins.PointHTMLTooltip(lines[0], labels=labels, voffset=10, hoffset=10)
    mpld3.plugins.connect(plt.gcf(), tooltips)
    plt.legend()
    plt.title(f'Stock: {symbol} Average Accuracy: {np.mean(accuracies):.4f}')
    ax = plt.gca()
    ax.set_facecolor("white")
    plt.xticks([])
    plt.autoscale(enable=True, axis='both', tight=None)
    html = mpld3.fig_to_html(plt.gcf())
    return html
