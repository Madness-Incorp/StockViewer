import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import yfinance as yf


class StockGraph():
    def createGraph(stockTicker, root):
        stock_for_graph = yf.Ticker(stockTicker)
        hist = stock_for_graph.history(period="1y")

        figure2 = plt.Figure(figsize=(5, 4), dpi=100)
        ax2 = figure2.add_subplot(111)

        ax2.yaxis.tick_right()
        ax2.yaxis.set_label_position("right")

        for widget in root.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(figure2, root)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill='both')

        # Plot the 'Close' price of Tesla stock
        hist['Close'].plot(kind="line", ax=ax2, color="r", marker="", fontsize=10)
        ax2.set_title(f"{stockTicker} + Stock Price (1 Year)")

        figure2.tight_layout()
