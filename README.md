# Gandalf-AI-GUI

**Stock Market Prediction & Trading Bot AI with a Web Interface**

---

## 📈 Stock Market Prediction using an LSTM Network

Long Short Term Memory networks – usually just called “LSTMs” – are a special kind of RNN, capable of learning long-term dependencies. They were introduced by Hochreiter & Schmidhuber (1997), and were refined and popularized by many people in following work. They work tremendously well on a large variety of problems, and are now widely used. LSTMs are explicitly designed to avoid the vanishing gradient problem.

<p align="center">
  <img src="https://github.com/crypto-code/Stock-Market-AI-GUI/blob/master/assets/lstm_model.png" alt="LSTM Model" width="600"/>
</p>

All recurrent neural networks have the form of a chain of repeating modules of neural network. In standard RNNs, this repeating module will have a very simple structure, such as a single tanh layer. LSTMs also have this chain-like structure, but the repeating module has a different architecture. Instead of having a single neural network layer, there are four, interacting in a very special way.

🔗 [Understanding LSTMs - Colah's Blog](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)

---

## 🤖 Stock Market Agent using Evolution Strategy Agent

Even though the name sounds fancy, under the hood, it’s perhaps the simplest algorithm you can devise for exploring a landscape. Consider an agent in an environment (like Pong) that’s implemented via a neural network. It takes pixels in the input layer and outputs probabilities of actions available to it (move the paddle up, down, or do nothing).

<p align="center">
  <img src="https://github.com/crypto-code/Stock-Market-AI-GUI/blob/master/assets/evolve_agent.png" alt="Evolution Strategy Agent" width="600"/>
</p>

Our task in reinforcement learning is to find the parameters (weights and biases) of the neural network that make the agent win more often and hence get more rewards.

🔗 [Reinforcement Learning without Gradients - Towards Data Science](https://towardsdatascience.com/reinforcement-learning-without-gradients-evolving-agents-using-genetic-algorithms-8685817d84f)

---

## 🛠️ Requirements

Ensure you have the following installed:

- **Python 3.6.2**: [Download](https://www.python.org/downloads/release/python-362/)
- **Django**: [Installation Guide](https://www.djangoproject.com/)
- **Numpy**: [PyPI](https://pypi.org/project/numpy/)
- **Tensorflow**: [PyPI](https://pypi.org/project/tensorflow/)
- **Keras**: [PyPI](https://pypi.org/project/Keras/)
- **Seaborn**: [PyPI](https://pypi.org/project/seaborn/)
- **Yahoo-Finance**: [PyPI](https://pypi.org/project/yahoo-finance/)
- **Pandas**: [PyPI](https://pypi.org/project/pandas/)
- **Matplotlib**: [PyPI](https://pypi.org/project/matplotlib/)

---

## 🚀 Usage

### 1. Start the Django Server

First, start the Django server using the following command:

```bash
python manage.py runserver
