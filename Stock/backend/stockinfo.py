import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import os
import pickle
from datetime import datetime

def get_symbols():
    """Load stock symbols from a pickle file."""
    try:
        module_dir = os.path.dirname(__file__)  # Get current directory
        file_path = os.path.join(module_dir, 'all_symbols.pkl')
        with open(file_path, 'rb') as file:
            symbols = pickle.load(file)
        return symbols
    except FileNotFoundError:
        raise FileNotFoundError("Symbol file 'all_symbols.pkl' not found.")
    except pickle.UnpicklingError:
        raise ValueError("Error unpickling the symbols file.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred while loading symbols: {str(e)}")

all_symbols = get_symbols()

def stock_today(symbol):
    """Fetch today's stock data and return HTML for plotting."""
    try:
        df = yf.download(symbol, period="1d", interval="1m")
        df.to_csv('data.csv')
        df = pd.read_csv('data.csv')

        if df.empty:
            raise ValueError(f"No data found for symbol: {symbol}")

        close = [round(x[0], 2) for x in df.iloc[:, 4:5].astype('float32').values.tolist()]
        date_ori = [x[11:-6] for x in df.iloc[:, 0].tolist()]

        labels = [f"""
            <table style="border: 1px solid black; font-weight:bold; font-size:larger; background-color:white">
            <tr style="border: 1px solid black;">
            <th style="border: 1px solid black;">Time:</th>
            <td style="border: 1px solid black;">{x}</td>
            </tr>
            <tr style="border: 1px solid black;">
            <th style="border: 1px solid black;">Close:</th>
            <td style="border: 1px solid black;">{y}</td>
            </tr>
            </table>
        """ for x, y in zip(date_ori, close)]

        fig, ax = plt.subplots(figsize=(11, 5))
        lines = plt.plot(date_ori, close, marker="*", mec='w', mfc='blue', label='Close', c='lightblue')
        plt.legend()
        plt.locator_params(axis='y', nbins=6)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y")
        plt.title(f"Stock: {symbol} Date: {dt_string}")
        plt.tight_layout()
        ax.grid(False)
        ax.set_facecolor("white")

        if close:  # Check if close is not empty
            plt.fill_between(date_ori, close, min(close), color='#0083f2')
        else:
            print("Error: The 'close' list is empty.")

        tooltips = mpld3.plugins.PointHTMLTooltip(lines[0], labels=labels, voffset=10, hoffset=10)
        mpld3.plugins.connect(plt.gcf(), tooltips)
        html = mpld3.fig_to_html(fig)
        return html
    except Exception as e:
        raise Exception(f"An error occurred while fetching today's stock data: {str(e)}")

def get_stock(symbol, period):
    """Fetch historical stock data for a given period and return HTML for plotting."""
    try:
        if period == "5d":
            df = yf.download(symbol, period=period, interval="5m")
        elif period == "1mo":
            df = yf.download(symbol, period=period, interval="90m")
        else:
            df = yf.download(symbol, period=period)

        df.to_csv('data.csv')
        df = pd.read_csv('data.csv')

        if df.empty:
            raise ValueError(f"No data found for symbol: {symbol}")

        close = [round(x[0], 2) for x in df.iloc[:, 4:5].astype('float32').values.tolist()]
        if period in ["5d", "1mo"]:
            date_ori = [x[:-9] for x in df.iloc[:, 0].tolist()]
        else:
            date_ori = [x for x in df.iloc[:, 0].tolist()]

        if period == "1y":
            date_ori = date_ori[0::5]
            close = close[0::5]
        elif period == "5y":
            date_ori = date_ori[0::20]
            close = close[0::20]
        elif period == "max":
            date_ori = date_ori[0::60]
            close = close[0::60]

        labels = [f"""
            <table style="border: 1px solid black; font-weight:bold; font-size:larger; background-color:white">
            <tr style="border: 1px solid black;">
            <th style="border: 1px solid black;">Date:</th>
            <td style="border: 1px solid black;">{x}</td>
            </tr>
            <tr style="border: 1px solid black;">
            <th style="border: 1px solid black;">Close:</th>
            <td style="border: 1px solid black;">{y}</td>
            </tr>
            </table>
        """ for x, y in zip(date_ori, close)]

        fig, ax = plt.subplots(figsize=(11, 5))
        lines = plt.plot(date_ori, close, marker="*", mec='w', mfc='blue', label='Close', c='lightblue')
        plt.legend()
        plt.locator_params(axis='y', nbins=6)
        plt.title(f"Stock: {symbol} Period: {period}")
        plt.tight_layout()
        ax.grid(False)
        ax.set_facecolor("white")
        plt.fill_between(date_ori, close, min(close), color='#0083f2')

        tooltips = mpld3.plugins.PointHTMLTooltip(lines[0], labels=labels, voffset=10, hoffset=10)
        mpld3.plugins.connect(plt.gcf(), tooltips)
        html = mpld3.fig_to_html(fig)
        return html
    except Exception as e:
        raise Exception(f"An error occurred while fetching historical stock data: {str(e)}")

def get_info(symbol):
    """Fetch basic information about a stock."""
    try:
        tick = yf.Ticker(symbol)
        hist = tick.history(period="1d")  # Changed from "2d" to "1d"

        if hist.empty:
            raise ValueError(f"No data found for symbol: {symbol}")

        stock = {
            "symbol": symbol,
            "name": next((s["name"] for s in all_symbols if s["symbol"] == symbol), "Unknown"),
            "close": round(hist["Close"].tolist()[-1], 2),
            "open": round(hist["Open"].tolist()[-1], 2),
            "change": round(hist["Close"].tolist()[-1] - hist["Close"].tolist()[0], 2),
            "pchange": round((hist["Close"].tolist()[-1] - hist["Close"].tolist()[0]) / hist["Close"].tolist()[0] * 100, 2),
            "color": "#00d600" if hist["Close"].tolist()[-1] > hist["Close"].tolist()[0] else "red",
            "volume": hist["Volume"].tolist()[-1]
        }
        return stock
    except Exception as e:
        raise Exception(f"An error occurred while fetching stock info: {str(e)}")
