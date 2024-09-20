from tkinter import messagebox
import csv
import customtkinter as ctk
import os
import Helpers as hp
import Main as main
import yfinance as yf


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
        self.search_entry.bind('<Return>', self.validateCSV)

    def validateCSV(self, event):
        csvLocation = self.search_entry.get().strip()

        doesExist = os.path.isfile(csvLocation)

        if not doesExist:
            messagebox.showerror('Error', 'CSV File does not exist')
        else:
            print('CSV File location:', csvLocation)
            main.csvLocation = csvLocation
            self.findStockTickers()
        self.destroy()

    def findStockTickers(self):
        csvTickers = []
        with open(main.csvLocation) as csvFile:
            reader = csv.reader(csvFile, delimiter=',')
            for row in reader:
                csvTickers.append(row[3])
        csvTickers.pop(0)
        self.add_selected_stocks(csvTickers)

    def fetch_stock_data(self, ticker):
        global actStock
        stock = yf.Ticker(ticker)
        actStock = stock
        try:
            info = stock.info
            return f"{info['symbol']} - {info['shortName']}"
        except Exception:
            return None

    def add_selected_stocks(self, tickers):
        for ticker in tickers:
            if ticker in main.tickerMap:
                messagebox.showwarning("Warning", "Stock already selected")
                return
            result = self.fetch_stock_data(ticker)
            if result:
                self.add_stock_to_parent(ticker, actStock)
            else:
                messagebox.showerror("Error", "Ticker could not be found")

    def add_stock_to_parent(self, stock_info, orgTicker):
        price = hp.getStockPrice(orgTicker)
        self.parent.create_stockBox(stock_info, price, 1)

def create_window(parent):
    CSVHelpers(parent).mainloop()



