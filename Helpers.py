import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
import yfinance as yf

class Extra(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title('Choose Stock')
        self.geometry('1000x1000')
        self.attributes('-topmost', True)

        search_frame = ctk.CTkFrame(self)
        search_frame.pack()

        self.search_Entry = ctk.CTkEntry(search_frame, placeholder_text="Enter Stock Ticker")
        self.search_Entry.pack()

        search_Button = ctk.CTkButton(search_frame, text="Search", command=self.search_stock)
        search_Button.pack()

        result_frame = ctk.CTkFrame(self)
        result_frame.pack()

        self.result_listBox = ctk.CTkTextbox(result_frame, width=50, height=10)
        self.result_listBox.pack(pady=10)

        selected_stock_frame = ctk.CTkFrame(self)
        selected_stock_frame.pack(pady=20)

        selected_stock_label = ctk.CTkLabel(selected_stock_frame, text="Selected Stocks: ")
        selected_stock_label.pack(pady=10)

        self.selected_stock_listbox = ctk.CTkTextbox(selected_stock_frame, width=50, height=10)
        self.selected_stock_listbox.pack(pady=10)

        self.result_listBox.bind('<Double-1>', self.add_selected_stock)

    def fetch_stock_data(self, ticker):
        stock = yf.Ticker(ticker)
        try:
            info = stock.info
            self.result_listBox.delete('1.0', tk.END)
            self.result_listBox.insert(tk.END, f"{info['symbol']} - {info['shortName']}")
        except Exception as e:
            self.result_listBox.delete('1.0', tk.END)
            self.result_listBox.insert(tk.END, "Ticker could not be found")

    def search_stock(self):
        ticker = self.search_Entry.get()
        self.fetch_stock_data(ticker)

    def add_selected_stock(self, event):
        selected = self.result_listBox.get('1.0', tk.END).strip()
        if selected and selected != "Ticker could not be found":
            self.selected_stock_listbox.insert(tk.END, selected + "\n")

def create_window():
    stock_chooser_window = Extra()
    stock_chooser_window.mainloop()

