import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import yfinance as yf
import mplcursors
from matplotlib.pyplot import arrow


class StockGraph():
    @staticmethod
    def create_graph(stock_ticker, root):
        stock_for_graph = yf.Ticker(stock_ticker)
        hist = stock_for_graph.history(period="1y")

        figure2 = plt.Figure(figsize=(5, 4), dpi=100)
        ax2 = figure2.add_subplot(111)

        dark_grey = "#333333"
        blue_color = "#007bff"

        figure2.patch.set_facecolor(dark_grey)
        ax2.patch.set_facecolor(dark_grey)

        ax2.spines['bottom'].set_color(blue_color)
        ax2.spines['top'].set_color(dark_grey)
        ax2.spines['right'].set_color(blue_color)
        ax2.spines['left'].set_color(dark_grey)

        ax2.xaxis.label.set_color(blue_color)
        ax2.yaxis.label.set_color(blue_color)

        ax2.tick_params(axis='x', colors=blue_color)
        ax2.tick_params(axis='y', colors=blue_color)

        # Enable right-side ticks and labels for the prices
        ax2.yaxis.tick_right()
        ax2.yaxis.set_label_position("right")

        ax2.set_title(f"{stock_ticker} Stock Price (1 Year)", color='white', fontsize=16)
        ax2.set_xlabel('Date', color=blue_color, fontsize=12)
        ax2.set_ylabel('Price', color=blue_color, fontsize=12)

        # Clear any existing widgets in the root container
        for widget in root.winfo_children():
            widget.destroy()

        # Create the canvas to render the matplotlib figure in Tkinter
        canvas = FigureCanvasTkAgg(figure2, root)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill='both')

        # Plot the 'Close' price of the stock
        line = hist['Close'].plot(kind="line", ax=ax2, color="green", marker="", fontsize=10)

        ax2.tick_params(left=False, labelleft=False)

        # Add hover functionality to show price information using mplcursors
        cursor = mplcursors.cursor(line, hover=True)


        @cursor.connect("add")
        def on_add(sel):
            sel.annotation.set_text(f'Price: {sel.target[1]:.2f}')

        # Make sure the layout is tight so elements are displayed properly
        figure2.tight_layout()
