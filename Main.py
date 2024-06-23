import tkinter as tk
import customtkinter as ctk
import Helpers as hp
import yfinance as yf

class Main(ctk.CTk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.geometry('1400x800')

        # Configure column weights for fixed width left column
        self.grid_columnconfigure(0, weight=1)  # Left column (fixed width)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight = 1)  # Middle and Right columns (combined weight)

        # Create frame objects for each column
        self.left_column = LeftColumn(self)
        self.middle_column = MiddleColumn(self)
        self.right_column = RightColumn(self)

        # Add frames to the grid layout
        self.left_column.grid(row=0, column=0, sticky="nsew")
        self.middle_column.grid(row=0, column=1, sticky="nsew")
        self.right_column.grid(row=0, column=2, sticky="nsew")

        self.mainloop()

class LeftColumn(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)  

        self.leftTopFrame = ctk.CTkFrame(self)
        self.leftTopFrame.pack(fill='both', expand=False)

        # Add UI elements for the left column here (buttons, labels, etc.)
        self.navigation_label = ctk.CTkLabel(self.leftTopFrame, text="Stocks", fg_color='grey', bg_color='grey')
        self.navigation_label.pack()

        self.adder_button = ctk.CTkButton(self.leftTopFrame, text="+", bg_color='grey', fg_color='grey', text_color='green', width=10, height=10, corner_radius=10, command=self.open_stock_chooser)
        self.adder_button.pack(side='right', pady=10)

        self.stocksFrame = ctk.CTkFrame(self, width = 10)
        self.stocksFrame.pack(fill='both', expand=False, pady=10)

    def open_stock_chooser(self):
        hp.create_window(self)

    def create_stockBox(self, ticker, tickerPrice):
        stock_box = ctk.CTkFrame(self.stocksFrame, height=50, width=10)
        stock_box.columnconfigure(0, weight=1)
        stock_box.columnconfigure(1, weight=1)
        stock_box.pack(fill='x', pady=2)  # Keep pack for horizontal fill

        stock_box_label = ctk.CTkLabel(stock_box, text=ticker)
        stock_box_label.place(relx=0, rely=0, relwidth=0.5, relheight=1)  # Use place with relative positioning

        stock_box_price = ctk.CTkLabel(stock_box, text=f"${tickerPrice:.2f}")
        stock_box_price.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

        stock_box.pack_propagate(False)

class MiddleColumn(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        # Add UI elements for the middle column here (main content, charts, etc.)
        self.stock_info_label = ctk.CTkLabel(self, text="Stock Information")
        self.stock_info_label.pack()
        # (Add other UI elements for the middle column)

class RightColumn(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        # Add UI elements for the right column here (watchlists, settings, etc.)
        self.watchlist_label = ctk.CTkLabel(self, text="News")
        self.watchlist_label.pack()
        # (Add other UI elements for the right column)

if __name__ == "__main__":
    Main('Stock Viewer')
