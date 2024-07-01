import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import yfinance as yf

# Fetch Tesla stock data
tsla = yf.Ticker("TSLA")
hist = tsla.history(period="1y")

# Create the main Tkinter window
root = tk.Tk()

# Create a figure for plotting
figure2 = plt.Figure(figsize=(5, 4), dpi=100)
ax2 = figure2.add_subplot(111)

# Create a FigureCanvasTkAgg widget to display the plot
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

# Plot the 'Close' price of Tesla stock
hist['Close'].plot(kind="line", legend=True, ax=ax2, color="r", marker="o", fontsize=10)
ax2.set_title("Tesla Stock Price (1 Year)")

# Start the Tkinter event loop
root.mainloop()
