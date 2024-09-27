# Gandalf-AI


# Stock-Market-AI-GUI
Stock Market Prediction &amp; Trading Bot using AI with a Web Interface

## Stock Market Prediction using an LSTM Network
Long Short Term Memory networks – usually just called “LSTMs” – are a special kind of RNN, capable of learning long-term dependencies. They were introduced by Hochreiter & Schmidhuber (1997), and were refined and popularized by many people in following work. They work tremendously well on a large variety of problems, and are now widely used. LSTMs are explicitly designed to avoid the vanishing gradient problem. 

<p align="center">
<img src="https://github.com/crypto-code/Stock-Market-AI-GUI/blob/master/assets/lstm_model.png" align="middle" />  
</p>

All recurrent neural networks have the form of a chain of repeating modules of neural network. In standard RNNs, this repeating module will have a very simple structure, such as a single tanh layer. LSTMs also have this chain-like structure, but the repeating module has a different structure. Instead of having a single neural network layer, there are four, interacting in a very special way.

For more info check out this [article](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)

## Stock Market Agent using Evolution Strategy Agent

Even though the name sounds fancy, under the hood, it’s perhaps the simplest algorithm you can devise for exploring a landscape. Consider an agent in an environment (like Pong) that’s implemented via a neural network. It takes pixels in the input layer and outputs probabilities of actions available to it (move the paddle up, down, or do nothing).

<p align="center">
<img src="https://github.com/crypto-code/Stock-Market-AI-GUI/blob/master/assets/evolve_agent.png" align="middle" />  
</p>

Our task in reinforcement learning is to find the parameters (weights and biases) of the neural network that make the agent win more often and hence get more rewards. 

For more info check out this [article](https://towardsdatascience.com/reinforcement-learning-without-gradients-evolving-agents-using-genetic-algorithms-8685817d84f)

## Requirements
* Python 3.6.2 ([Download](https://www.python.org/downloads/release/python-362/))
* Django ([Homepage](https://www.djangoproject.com/))
* Numpy ([PyPI](https://pypi.org/project/numpy/))
* Tensorflow ([PyPI](https://pypi.org/project/tensorflow/))
* Keras ([PyPI](https://pypi.org/project/Keras/))
* Seaborn ([PyPI](https://pypi.org/project/seaborn/))
* Yahoo-Finance ([PyPI](https://pypi.org/project/yahoo-finance/))
* Pandas ([PyPI](https://pypi.org/project/pandas/))
* Matplotlib ([PyPI](https://pypi.org/project/matplotlib/))

## Usage

First, start the Django server using the following command:
```bash
python manage.py runserver
Main Page
<p align="center"> <img src="https://github.com/crypto-code/Stock-Market-AI-GUI/blob/master/assets/Main.PNG" align="middle" /> </p>
The main page gives you three options to choose from:

1. Stock Info
<p align="center"> <img src="https://github.com/crypto-code/Stock-Market-AI-GUI/blob/master/assets/Info.PNG" align="middle" /> </p> Just input the symbol of the stock and the duration for which to get the data. The data is fetched using the yahoo-finance library and graphed using matplotlib and mpld3. <p align="center"> <img src="https://github.com/crypto-code/Stock-Market-AI-GUI/blob/master/assets/Info-done.png" align="middle" /> </p> The details are shown in a table, and the closing prices are graphed. Hovering your mouse over the points will display a tooltip with the date and the closing price for that day.
2. Prediction
<p align="center"> <img src="https://github.com/crypto-code/Stock-Market-AI-GUI/blob/master/assets/Prediction.png" align="middle" /> </p> For the prediction, you need to input the symbol for the stock, the period of data to train with, the number of simulations to run, and the number of future days to predict. <p align="center"> <img src="https://github.com/crypto-code/Stock-Market-AI-GUI/blob/master/assets/Prediction-done.png" align="middle" /> </p> The closing prices of the simulations that are deemed acceptable are graphed using matplotlib and mpld3. Hovering your mouse over the points will display a tooltip with the date and the closing price for that day.
3. Trading Agent
<p align="center"> <img src="https://github.com/crypto-code/Stock-Market-AI-GUI/blob/master/assets/Agent.png" align="middle" /> </p> For the trading agent, you need to input the symbol for the stock, the period of data to trade on, the initial fund, and the number of days to skip between selling or buying. <p align="center"> <img src="https://github.com/crypto-code/Stock-Market-AI-GUI/blob/master/assets/Agent-done.png" align="middle" /> </p> The closing prices are graphed, and the selling and buying days are marked with their respective markers using matplotlib and mpld3. Hovering your mouse over the marker will display the date and the action taken on that day. ```
Additional Recommendations:
Dependencies Management:

Ensure that all required packages are listed in your requirements.txt with the correct versions to maintain consistency across different environments.
Consider using virtual environments (like venv or conda) to manage dependencies effectively.
Python Version:

Python 3.6.2 is quite outdated. It's recommended to upgrade to a newer version (e.g., Python 3.8 or later) to benefit from improved features and security updates.
Django Configuration:

Ensure that your Django settings are configured for production if you intend to deploy the application. This includes settings for security, allowed hosts, database configurations, etc.
AI Models:

Document the architecture of your LSTM and Evolution Strategy agents in more detail if possible.
Include instructions on how to train these models, including any preprocessing steps required.
Usage Instructions:

Provide detailed steps on how to set up the project locally, including cloning the repository, setting up the environment, installing dependencies, and running migrations if necessary.
Include any environment variables or configurations that need to be set.
Contributing Guidelines:

If you welcome contributions, consider adding a CONTRIBUTING.md file to guide contributors on how to submit issues or pull requests.
License:

Specify the license under which your project is distributed to inform users and contributors of their rights and responsibilities.
Contact Information:

Provide a way for users to reach out for support or inquiries, such as an email address or a link to a discussion forum.

