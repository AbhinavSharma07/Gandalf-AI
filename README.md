# Gandalf-AI
# 📈 Stock-Market-AI-GUI

**Stock Market Prediction & Trading Bot using AI with a Web Interface**

![Project Banner](https://github.com/crypto-code/Stock-Market-AI-GUI/blob/master/assets/banner.png)

## 🚀 Overview

Welcome to **Stock-Market-AI-GUI**, a comprehensive application that leverages AI to predict stock market trends and execute trading strategies. Built with a user-friendly web interface, this tool integrates advanced machine learning models to provide insightful stock analyses and automated trading capabilities.

---

## 📚 Table of Contents

- [📈 Stock Market Prediction using an LSTM Network](#stock-market-prediction-using-an-lstm-network)
- [🤖 Stock Market Agent using Evolution Strategy](#stock-market-agent-using-evolution-strategy)
- [🛠️ Features](#features)
- [📝 Requirements](#requirements)
- [💻 Installation](#installation)
- [🚀 Usage](#usage)
  - [1. Main Page](#1-main-page)
  - [2. Stock Info](#2-stock-info)
  - [3. Prediction](#3-prediction)
  - [4. Trading Agent](#4-trading-agent)
- [🔗 Links](#links)
- [🧑‍💻 Contributing](#contributing)
- [📝 License](#license)

---

## 📈 Stock Market Prediction using an LSTM Network

Long Short Term Memory networks (**LSTMs**) are a special kind of Recurrent Neural Network (RNN), capable of learning long-term dependencies. Introduced by Hochreiter & Schmidhuber in 1997, LSTMs were refined and popularized by subsequent research, making them a staple in various AI applications today.

![LSTM Model](https://github.com/crypto-code/Stock-Market-AI-GUI/blob/master/assets/lstm_model.png)

**Key Points:**
- **Chain-like Structure:** Similar to standard RNNs but with a more complex repeating module.
- **Avoids Vanishing Gradient Problem:** Designed to retain information over longer periods.
- **Versatility:** Widely used across different domains for tasks involving sequence prediction.

For an in-depth understanding, check out this [Comprehensive Article on LSTMs](https://colah.github.io/posts/2015-08-Understanding-LSTMs/).

---

## 🤖 Stock Market Agent using Evolution Strategy

Our **Evolution Strategy Agent** employs a straightforward yet effective algorithm for navigating complex environments. This approach is particularly useful in reinforcement learning scenarios where the goal is to optimize the agent's performance over time.

![Evolution Strategy Agent](https://github.com/crypto-code/Stock-Market-AI-GUI/blob/master/assets/evolve_agent.png)

**How It Works:**
1. **Agent Environment:** The agent interacts with the stock market environment, making decisions based on input data.
2. **Neural Network:** Processes inputs (e.g., stock prices) and outputs action probabilities (e.g., buy, sell, hold).
3. **Evolutionary Optimization:** Iteratively adjusts the network's parameters to maximize rewards (e.g., profits).

Learn more about this method in this [Reinforcement Learning Article](https://towardsdatascience.com/reinforcement-learning-without-gradients-evolving-agents-using-genetic-algorithms-8685817d84f).

---

## 🛠️ Features

- **Interactive Web Interface:** User-friendly Django-based GUI for seamless interaction.
- **Real-Time Stock Data:** Fetches and displays live stock information using Yahoo Finance.
- **AI-Powered Predictions:** Utilizes LSTM networks to forecast future stock prices.
- **Automated Trading Bot:** Implements Evolution Strategy Agents for executing trades based on AI insights.
- **Dynamic Visualizations:** Interactive charts and graphs created with Matplotlib and mpld3 for data visualization.

---

## 📝 Requirements

Ensure you have the following installed before setting up the project:

- **Python 3.6.2**  
  [Download Python](https://www.python.org/downloads/release/python-362/)
  
- **Django**  
  [Django Documentation](https://www.djangoproject.com/)
  
- **Numpy**  
  [Numpy on PyPI](https://pypi.org/project/numpy/)
  
- **TensorFlow**  
  [TensorFlow on PyPI](https://pypi.org/project/tensorflow/)
  
- **Keras**  
  [Keras on PyPI](https://pypi.org/project/Keras/)
  
- **Seaborn**  
  [Seaborn on PyPI](https://pypi.org/project/seaborn/)
  
- **Yahoo-Finance**  
  [Yahoo-Finance on PyPI](https://pypi.org/project/yahoo-finance/)
  
- **Pandas**  
  [Pandas on PyPI](https://pypi.org/project/pandas/)
  
- **Matplotlib**  
  [Matplotlib on PyPI](https://pypi.org/project/matplotlib/)

---

## 💻 Installation

Follow these steps to set up the project locally:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/crypto-code/Stock-Market-AI-GUI.git
   cd Stock-Market-AI-GUI
