import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
import yfinance as yf
import Main as main

class Extra(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title('Choose Stock')
        self.geometry('800x600')
        self.attributes('-topmost', True)

        # Search Frame
        search_frame = ctk.CTkFrame(self)
        search_frame.pack(pady=20)

        self.search_entry = ctk.CTkEntry(search_frame, placeholder_text="Enter Stock Ticker", width=300)
        self.search_entry.pack(padx=10)
        self.search_entry.bind('<Return>', self.add_selected_stock)

        # Selected Stock Frame
        selected_stock_frame = ctk.CTkFrame(self)
        selected_stock_frame.pack(pady=20)

        selected_stock_label = ctk.CTkLabel(selected_stock_frame, text="Selected Stocks:")
        selected_stock_label.pack(pady=5)

        self.selected_stock_listbox = tk.Listbox(selected_stock_frame, width=50, height=10)
        self.selected_stock_listbox.pack(pady=10)

        self.selected_stocks = set()  # To keep track of selected stocks

    def fetch_stock_data(self, ticker):
        stock = yf.Ticker(ticker)
        try:
            info = stock.info
            return f"{info['symbol']} - {info['shortName']}"
        except Exception:
            return None

    def add_selected_stock(self, event):
        ticker = self.search_entry.get().strip().upper()
        if ticker in self.selected_stocks:
            messagebox.showwarning("Warning", "Stock already selected")
            return
        result = self.fetch_stock_data(ticker)
        if result:
            self.selected_stocks.add(ticker)
            self.selected_stock_listbox.insert(tk.END, result)
            self.search_entry.delete(0, tk.END)
            main.LeftColumn.create_stockBox(ticker)
        else:
            messagebox.showerror("Error", "Ticker could not be found")

def create_window():
    stock_chooser_window = Extra()
    stock_chooser_window.mainloop()

create_window()
