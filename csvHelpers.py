import subprocess
from tkinter import messagebox
import csv
import customtkinter as ctk
import os
import Helpers as hp
import Main as main
import yfinance as yf

from Global import set_csvLocationGlobal, get_csvLocationGlobal


def fetch_stock_data(ticker):
    global actStock
    stock = yf.Ticker(ticker)
    actStock = stock
    try:
        info = stock.info
        return f"{info['symbol']} - {info['shortName']}"
    except Exception:
        return None


class CSVHelpers(ctk.CTkToplevel):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.title('CSV File location')
        self.geometry('400x200')
        self.attributes('-topmost', True)

        # Search Frame
        search_frame = ctk.CTkFrame(self)
        search_frame.pack(pady=20)

        self.search_entry = ctk.CTkEntry(search_frame, placeholder_text="Please enter the CSV file location", width=400)
        self.search_entry.place(rely=0.4)
        self.search_entry.bind('<Return>', self.validate_csv)

    def validate_csv(self, event):
        csv_location = self.search_entry.get().strip()
        does_exist = os.path.isfile(csv_location)

        if not does_exist:
            messagebox.showerror('Error', 'CSV File does not exist')
        else:
            set_csvLocationGlobal(csv_location)
            print('CSV File location:', get_csvLocationGlobal())
            run_java(csv_location)
            self.find_stock_tickers(get_csvLocationGlobal())
        self.destroy()

    def find_stock_tickers(self, location):
        csv_tickers = []

        if location is None:
            messagebox.showerror('Error', 'CSV File location has not been set')
            return

        with open(location) as csvFile:
            reader = csv.reader(csvFile, delimiter=',')
            for row in reader:
                csv_tickers.append(row[3])
        csv_tickers.pop(0)
        self.add_selected_stocks(csv_tickers)

    def add_selected_stocks(self, tickers):
        for ticker in tickers:
            if ticker in main.tickersSeen:
                messagebox.showwarning("Warning", "Stock already selected")
                return
            result = fetch_stock_data(ticker)
            if result:
                self.add_stock_to_parent(ticker, actStock)
                main.tickersSeen.append(ticker)
            else:
                messagebox.showerror("Error", "Ticker could not be found")

    def add_stock_to_parent(self, stock_info, original_ticker):
        price = hp.get_stock_price(original_ticker)
        self.parent.create_stock_box(stock_info, price, 1)

def create_window(parent):
    CSVHelpers(parent).mainloop()

def run_java(location_of_csv):
    subprocess.Popen(['java', 'Take_Data', location_of_csv])




