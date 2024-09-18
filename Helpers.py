import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import yfinance as yf
import Main as main

global current

class Extra(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.title('Choose Stock')
        self.geometry('400x200')
        self.attributes('-topmost', True)

        # Search Frame
        search_frame = ctk.CTkFrame(self)
        search_frame.pack(pady=20)

        self.search_entry = ctk.CTkEntry(search_frame, placeholder_text="Enter Stock Ticker", width=400)
        self.search_entry.place(rely = 0.4)
        self.search_entry.bind('<Return>', self.add_selected_stock)

    def fetch_stock_data(self, ticker):
        global actStock
        stock = yf.Ticker(ticker)
        actStock = stock
        try:
            info = stock.info
            return f"{info['symbol']} - {info['shortName']}"
        except Exception:
            return None

    def add_selected_stock(self, event):
        ticker = self.search_entry.get().strip().upper()
        global current
        current = ticker
        if ticker in main.tickerMap:
            messagebox.showwarning("Warning", "Stock already selected")
            return
        result = self.fetch_stock_data(ticker)
        if result:
            self.search_entry.delete(0, tk.END)
            self.add_stock_to_parent(ticker, actStock)
        else:
            messagebox.showerror("Error", "Ticker could not be found")

    def add_stock_to_parent(self, stock_info, orgTicker):
        price = getStockPrice(orgTicker)
        self.parent.create_stockBox(stock_info, price, 0)
        self.destroy()

def getStockPrice(stock):
        ticker = stock

        # Try to fetch data for today
        stockPrice = ticker.history(period='1d')

        # If no data for today, fetch data for the previous days until one is found
        if stockPrice.empty:
            for i in range(2, 5):  # Adjust the range based on your needs
                stockPrice = ticker.history(period=f'{i}d')
                if not stockPrice.empty:
                    break

        if stockPrice.empty:
            raise ValueError(f"No data available for {stock} for today or the past 4 days.")

        # Get the latest available close price
        latest_price = stockPrice['Close'].iloc[-1]

        return latest_price    

def create_window(parent):
    stock_chooser_window = Extra(parent)
    stock_chooser_window.mainloop()

        
