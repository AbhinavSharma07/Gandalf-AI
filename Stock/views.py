from django.shortcuts import render
from django.http import JsonResponse
from Stock.backend.stockinfo import *
from Stock.backend.predict import *
from Stock.backend.trade import *
import time

# Create your views here.

def index(request):
    return render(request, "index.html")

def stock(request):
    data = None
    stock = None
    if request.method == "POST":
        sym = request.POST["symbol"]
        period = request.POST["period"]  # Corrected variable name to 'period'
        if period == "1d":
            data = stock_today(sym)
        else:
            data = get_stock(sym, period)
        stock = get_info(sym)

    context = {
        "data": data,
        "symbols": all_symbols,
        "stock": stock
    }
    return render(request, "stock.html", context)

def stock_predict(request, symbol, period, sim, future):
    data = predict_stock(symbol, period, sim, future)
    return JsonResponse({"data": data})

def predict(request):
    data = None
    sym = ""
    if request.method == "POST":
        sym = request.POST["symbol"]
        data = predict_stock(sym, request.POST["period"], request.POST["sim"], request.POST["future"])  # Assuming you want to process this

    context = {
        "symbols": all_symbols,
        "data": data,
        "sym": sym
    }
    return render(request, "predict.html", context)

def stock_trade(request, symbol, period, init, skip):
    # Add try-except block to handle potential errors
    try:
        data = trade_stock(symbol, period, float(init), int(skip))  # Make sure init and skip are appropriately converted
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
    
    time.sleep(5)  # Simulate processing delay if needed
    return JsonResponse({"data": data})

def trade(request):
    data = None
    sym = ""
    if request.method == "POST":
        sym = request.POST["symbol"]
        # Use 'initial' instead of 'init' to match the form field name
        data = trade_stock(sym, request.POST["period"], float(request.POST["initial"]), int(request.POST["no_days"]))  # 'initial' and 'no_days'

    context = {
        "symbols": all_symbols,
        "data": data,
        "sym": sym
    }
    return render(request, "trade.html", context)
