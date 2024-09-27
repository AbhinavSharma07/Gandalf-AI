import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt, mpld3
import os
import yfinance as yf

def trade_stock(symbol, period, init, skip):
    # Fetch data using yf.download() instead of pdr.get_data_yahoo()
    df = yf.download(symbol, period=period)

    class Deep_Evolution_Strategy:
        inputs = None

        def __init__(self, weights, reward_function, population_size, sigma, learning_rate):
            self.weights = weights
            self.reward_function = reward_function
            self.population_size = population_size
            self.sigma = sigma
            self.learning_rate = learning_rate

        def _get_weight_from_population(self, weights, population):
            weights_population = []
            for index, i in enumerate(population):
                jittered = self.sigma * i
                weights_population.append(weights[index] + jittered)
            return weights_population

        def get_weights(self):
            return self.weights

        def train(self, epoch=100, print_every=1):
            lasttime = time.time()
            for i in range(epoch):
                population = []
                rewards = np.zeros(self.population_size)
                for k in range(self.population_size):
                    x = []
                    for w in self.weights:
                        x.append(np.random.randn(*w.shape))
                    population.append(x)
                for k in range(self.population_size):
                    weights_population = self._get_weight_from_population(self.weights, population[k])
                    rewards[k] = self.reward_function(weights_population)
                rewards = (rewards - np.mean(rewards)) / (np.std(rewards) + 1e-7)
                for index, w in enumerate(self.weights):
                    A = np.array([p[index] for p in population])
                    self.weights[index] = (
                        w
                        + self.learning_rate
                        / (self.population_size * self.sigma)
                        * np.dot(A.T, rewards).T
                    )
                if (i + 1) % print_every == 0:
                    print('iter %d. reward: %f' % (i + 1, self.reward_function(self.weights)))
            print('time taken to train:', time.time() - lasttime, 'seconds')

    class Model:
        def __init__(self, input_size, layer_size, output_size):
            self.weights = [
                np.random.randn(input_size, layer_size),
                np.random.randn(layer_size, output_size),
                np.random.randn(1, layer_size),
            ]

        def predict(self, inputs):
            feed = np.dot(inputs, self.weights[0]) + self.weights[-1]
            decision = np.dot(feed, self.weights[1])
            return decision

        def get_weights(self):
            return self.weights

        def set_weights(self, weights):
            self.weights = weights

    class Agent:
        POPULATION_SIZE = 15
        SIGMA = 0.1
        LEARNING_RATE = 0.03

        def __init__(self, model, window_size, trend, skip, initial_money):
            self.model = model
            self.window_size = window_size
            self.half_window = window_size // 2
            self.trend = trend
            self.skip = skip
            self.initial_money = initial_money
            self.es = Deep_Evolution_Strategy(
                self.model.get_weights(),
                self.get_reward,
                self.POPULATION_SIZE,
                self.SIGMA,
                self.LEARNING_RATE,
            )

        def act(self, sequence):
            decision = self.model.predict(np.array(sequence))
            return np.argmax(decision[0])

        def get_state(self, t):
            window_size = self.window_size + 1
            d = t - window_size + 1
            block = self.trend[d : t + 1] if d >= 0 else -d * [self.trend[0]] + self.trend[0 : t + 1]
            res = []
            for i in range(window_size - 1):
                res.append(block[i + 1] - block[i])
            return np.array([res])

        def get_reward(self, weights):
            initial_money = self.initial_money
            starting_money = initial_money
            self.model.weights = weights
            state = self.get_state(0)
            inventory = []
            quantity = 0
            for t in range(0, len(self.trend) - 1, self.skip):
                action = self.act(state)
                next_state = self.get_state(t + 1)

                if action == 1 and starting_money >= self.trend[t]:
                    inventory.append(self.trend[t])
                    starting_money -= self.trend[t]

                elif action == 2 and len(inventory):
                    bought_price = inventory.pop(0)
                    starting_money += self.trend[t]

                state = next_state
            return ((starting_money - initial_money) / initial_money) * 100

        def fit(self, iterations, checkpoint):
            self.es.train(iterations, print_every=checkpoint)

        def buy(self):
            initial_money = self.initial_money
            state = self.get_state(0)
            starting_money = initial_money
            states_sell = {}
            states_buy = {}
            inventory = []
            for t in range(0, len(self.trend) - 1, self.skip):
                action = self.act(state)
                next_state = self.get_state(t + 1)

                if action == 1 and initial_money >= self.trend[t]:
                    inventory.append(self.trend[t])
                    initial_money -= self.trend[t]
                    states_buy[t] = f'Day {t}: Buy 1 unit at Price {self.trend[t]:.2f}, Total Balance {initial_money:.2f}'

                elif action == 2 and len(inventory):
                    bought_price = inventory.pop(0)
                    initial_money += self.trend[t]
                    invest = ((self.trend[t] - bought_price) / bought_price) * 100
                    states_sell[t] = f'Day {t}, Sell 1 unit at Price {self.trend[t]:.2f}, Investment {invest:.2f}%, Total Balance {initial_money:.2f}'

                state = next_state

            invest = ((initial_money - starting_money) / starting_money) * 100
            total_gains = initial_money - starting_money
            return states_buy, states_sell, total_gains, invest

    # Close price data for the stock
    close = df['Close'].values.tolist()
    df.to_csv('data.csv')
    df = pd.read_csv('data.csv')
    date_ori = pd.to_datetime(df.iloc[:, 0]).tolist()
    date_ori = pd.Series(date_ori).dt.strftime(date_format='%Y-%m-%d').tolist()

    # Hyperparameters for model
    window_size = 30
    initial_money = init
    model = Model(input_size=window_size, layer_size=500, output_size=3)
    agent = Agent(model=model, window_size=window_size, trend=close, skip=skip, initial_money=initial_money)
    agent.fit(iterations=100, checkpoint=10)  # Reduced iterations for quicker training

    # Perform the buy operation
    states_buy, states_sell, total_gains, invest = agent.buy()

    # Plotting the results
    fig = plt.figure(figsize=(11, 5))
    plt.plot(date_ori, close, color='r', lw=2.)
    
    # Buy signals
    buy = [close[t] if t in states_buy else None for t in range(len(close))]
    buy_labels = [f"Date: {date_ori[t]}<br>Action: {states_buy.get(t, '')}" for t in range(len(close))]
    lines = plt.plot(date_ori, buy, marker='^', markersize=10, color='m', label='buying signal')
    tooltips = mpld3.plugins.PointHTMLTooltip(lines[0], labels=buy_labels, voffset=10, hoffset=10)
    mpld3.plugins.connect(plt.gcf(), tooltips)

    # Sell signals
    sell = [close[t] if t in states_sell else None for t in range(len(close))]
    sell_labels = [f"Date: {date_ori[t]}<br>Action: {states_sell.get(t, '')}" for t in range(len(close))]
    lines = plt.plot(date_ori, sell, marker='v', markersize=10, color='k', label='selling signal')
    tooltips = mpld3.plugins.PointHTMLTooltip(lines[0], labels=sell_labels, voffset=10, hoffset=10)
    mpld3.plugins.connect(plt.gcf(), tooltips)

    plt.xticks([])
    plt.autoscale(enable=True, axis='both', tight=None)
    plt.title(f'Stock: {symbol} Total Gains: {total_gains:.2f}, Total Investment: {invest:.2f}%')
    plt.legend(fontsize="large")

    # Save the plot as HTML
    html = mpld3.fig_to_html(fig)
    os.remove("data.csv")
    
    return html
