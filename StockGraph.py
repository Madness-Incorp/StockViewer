import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import yfinance as yf
import mplcursors

class StockGraph():
    def createGraph(stockTicker, root):
        stock_for_graph = yf.Ticker(stockTicker)
        hist = stock_for_graph.history(period="1y")

        figure2 = plt.Figure(figsize=(5, 4), dpi=100)
        ax2 = figure2.add_subplot(111)

        figure2.patch.set_facecolor('black')

        ax2.yaxis.tick_right()
        ax2.yaxis.set_label_position("right")
        ax2.patch.set_facecolor('black')

        ax2.spines['bottom'].set_color('blue')
        ax2.spines['right'].set_color('blue')
        ax2.xaxis.label.set_color('blue')
        ax2.yaxis.label.set_color('blue')

        ax2.tick_params(axis='x', colors='blue')
        ax2.tick_params(axis='y', colors='blue')

        # Set the title and labels with colors
        ax2.set_title('Sample Plot', color='white')
        ax2.set_xlabel('X Axis', color='blue')
        ax2.set_ylabel('Y Axis', color='blue')

        for widget in root.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(figure2, root)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill='both')

        # Plot the 'Close' price of Tesla stock
        line = hist['Close'].plot(kind="line", ax=ax2, color="r", marker="", fontsize=10)
        ax2.set_title(f"{stockTicker} + Stock Price (1 Year)")

        ax2.tick_params(left=False, bottom=False, labelleft=False)

        cursor = mplcursors.cursor(line, hover=True)

        @cursor.connect("add")
        def on_add(sel):
            sel.annotation.set_text(f'Price: {sel.target[1]:.2f}')

        figure2.tight_layout()
