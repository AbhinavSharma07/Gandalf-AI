# Gandalf-AI-GUI

Stock Market Prediction & Trading Bot AI with an Interactive Web Interface

## Advanced Stock Market Prediction with LSTM Network

Long Short Term Memory (LSTM) networks are a revolutionary type of Recurrent Neural Networks (RNNs) known for their ability to capture long-term dependencies. Introduced by Hochreiter & Schmidhuber (1997), and refined over the years, LSTMs have become essential for solving complex sequential data problems. Unlike standard RNNs, LSTMs effectively tackle the vanishing gradient problem, making them ideal for stock market prediction.

<p align="center">
<img src="https://github.com/crypto-code/Stock-Market-AI-GUI/blob/master/assets/lstm_model.png" align="middle" />
</p>

All RNNs have a chain-like structure of repeating modules. While standard RNNs may consist of a single tanh layer, LSTMs have a more intricate architecture with four layers that interact in a distinctive way. This complexity allows LSTMs to perform exceptionally well in forecasting stock trends over long periods.

For an in-depth understanding, read this [comprehensive article](https://colah.github.io/posts/2015-08-Understanding-LSTMs/).

## Stock Market Agent Powered by Evolution Strategy

Evolution Strategy (ES) is a powerful, yet simple, method for optimizing a landscape of possible solutions. Imagine a trading agent in a dynamic environment that uses a neural network to decide the best actions (buy, sell, hold). This agent processes stock data and determines the probabilities of different market actions.

<p align="center">
<img src="https://github.com/crypto-code/Stock-Market-AI-GUI/blob/master/assets/evolve_agent.png" align="middle" />
</p>

In reinforcement learning, our goal is to optimize the neural network parameters (weights and biases) so that the agent maximizes its rewards (profits) over time. By using evolutionary strategies, we can bypass traditional gradient-based learning and evolve our trading agent in a more explorative and adaptive manner.

For a deeper dive into the methodology, check out this [insightful article](https://towardsdatascience.com/reinforcement-learning-without-gradients-evolving-agents-using-genetic-algorithms-8685817d84f).

## Requirements

Ensure you have the following software and libraries installed:

- **Python 3.6.2** (https://www.python.org/downloads/release/python-362/)
- **Django** (https://www.djangoproject.com/)
- **Numpy** (https://pypi.org/project/numpy/)
- **Tensorflow** (https://pypi.org/project/tensorflow/)
- **Keras** (https://pypi.org/project/Keras/)
- **Seaborn** (https://pypi.org/project/seaborn/)
- **Yahoo-Finance** (https://pypi.org/project/yahoo-finance/)
- **Pandas** (https://pypi.org/project/pandas/)
- **Matplotlib** (https://pypi.org/project/matplotlib/)

## Web Interface Overview

### Main Dashboard

<p align="center">
<img src="https://github.com/AbhinavSharma07/Gandalf-AI/blob/main/assets/Main.png" align="middle" />
</p>

The dashboard provides three primary functionalities for users:

### 1. **Stock Information**

<p align="center">
<img src="https://github.com/AbhinavSharma07/Gandalf-AI/blob/main/assets/Info.png" align="middle" />
</p>

Enter the stock symbol and the duration to retrieve historical data, which is fetched using the Yahoo Finance API. The data is then beautifully visualized using **matplotlib** and **mpld3**, allowing you to interact with the chart. Hover over points to see the stock's closing price and the date.

<p align="center">
<img src="https://github.com/AbhinavSharma07/Gandalf-AI/blob/main/assets/Info-done.png" align="middle" />
</p>

### 2. **Stock Price Prediction**

<p align="center">
<img src="https://github.com/AbhinavSharma07/Gandalf-AI/blob/main/assets/Prediction.png" align="middle" />
</p>

For predicting future stock prices, input the stock symbol, the historical period for training, the number of simulations to run, and the number of days to forecast. Gandalf-AI leverages LSTM models to generate predictions. The results are presented in an interactive graph, where you can hover over points to see the predicted prices for future dates.

<p align="center">
<img src="https://github.com/AbhinavSharma07/Gandalf-AI/blob/main/assets/Prediction-done.png" align="middle" />
</p>

### 3. **Trading Agent**

<p align="center">
<img src="https://github.com/AbhinavSharma07/Gandalf-AI/blob/main/assets/Agent.png" align="middle" />
</p>

In the trading agent interface, enter the stock symbol, the data period for analysis, the initial investment fund, and the trading interval (number of days between buy/sell decisions). Gandalf-AI’s Evolution Strategy-based agent will trade stocks automatically. The buying and selling points are marked on the graph, allowing users to visualize the trading strategy.

<p align="center">
<img src="https://github.com/AbhinavSharma07/Gandalf-AI/blob/main/assets/Agent-done.png" align="middle" />
</p>

## Usage Instructions

1. Start the Django server by running the following command:
   ```bash
   python manage.py runserver
