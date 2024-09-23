import threading
from tkinter import messagebox

import customtkinter as ctk
import Connection
import Helpers as hp
import StockGraph as sg
import csvHelpers as csvH

tickerMap = {}
tickersSeen = []

# Set global styles
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")  # Optional: Can help maintain consistent dark theme

class Main(ctk.CTk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.geometry('1000x400')
        self.configure(fg_color="#333333")

        # Configure column weights for fixed width left column
        self.grid_columnconfigure(0, weight=1)  # Left column (fixed width)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=1)  # Middle and Right columns (combined weight)

        # Create frame objects for each column
        self.left_column = LeftColumn(self)
        self.middle_column = MiddleColumn(self)
        self.right_column = RightColumn(self, self.left_column)

        # Add frames to the grid layout
        self.left_column.grid(row=0, rowspan=2, column=0, sticky="nsew")
        self.middle_column.grid(row=0, column=1, columnspan=2, sticky="nsew")
        self.right_column.grid(row=1, column=1, columnspan=2, sticky="nsew")

        self.left_column.set_middle_column(self.middle_column)

        self.mainloop()

class LeftColumn(ctk.CTkFrame):
    csvStockCreated = False

    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color="#333333")

        self.stock_label = None
        self.parent = parent
        self.middle_column = None

        self.leftTopFrame = ctk.CTkFrame(self, fg_color="#333333")
        self.leftTopFrame.pack(fill='both', expand=False)

        # Add UI elements for the left column here (buttons, labels, etc.)
        self.navigation_label = ctk.CTkLabel(self.leftTopFrame, text="Stocks", text_color="white", font=("Roboto", 20), fg_color="#333333")
        self.navigation_label.pack()

        # Plus button with green background and circular shape
        self.adder_button = ctk.CTkButton(
            self.leftTopFrame,
            text="+",
            fg_color="#00b300",
            text_color="white",
            width=30,
            height=30,
            corner_radius=15,
            font=("Roboto", 15),
            command=self.open_stock_chooser
        )
        self.adder_button.pack(side='right', pady=10)

        self.stocksFrame = ctk.CTkScrollableFrame(self, width=10, fg_color="#333333")
        self.stocksFrame.pack(fill='both', expand=True, pady=10)

    def open_stock_chooser(self):
        hp.create_window(self)

    def set_middle_column(self, middle_column):
        self.middle_column = middle_column

    def create_stock_box(self, ticker, ticker_price, flag):
        stock_box = ctk.CTkFrame(self.stocksFrame, height=50, width=10, fg_color="#333333")
        stock_box.columnconfigure(0, weight=1)
        stock_box.columnconfigure(1, weight=1)

        if self.csvStockCreated and flag == 1:
            stock_box.pack(after=self.stock_label, fill='x', pady=2)
        elif self.csvStockCreated and flag == 0:
            stock_box.pack(before=self.stock_label, fill='x', pady=2)
        else:
            stock_box.pack(fill='x', pady=2)


        stock_box_button = ctk.CTkButton(
            stock_box,
            text=f"{ticker}    ${ticker_price:.2f}",
            fg_color="#007bff",
            text_color="white",
            font=("Roboto", 12),
            corner_radius=10,
            command=lambda: self.print_graph(stock_box_button.winfo_id())
        )
        stock_box_button.place(relx=0, rely=0, relwidth=1, relheight=1)

        if flag == 0:
            tickerMap[stock_box_button.winfo_id()] = hp.current
        else:
            tickerMap[stock_box_button.winfo_id()] = ticker

        stock_box.pack_propagate(False)

    def print_graph(self, id):
        ticker = tickerMap[id]
        sg.StockGraph.create_graph(ticker, self.middle_column.stock_graph_frame)

    def add_stocks_csv(self):
        if not self.csvStockCreated:
            self.stock_label = ctk.CTkLabel(self.stocksFrame, text="Stocks from CSV", text_color="white", font=("Roboto", 20), fg_color="#333333")
            self.stock_label.pack()
        self.csvStockCreated = True
        csvH.create_window(self)


class MiddleColumn(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color="#333333")  # Dark grey background for middle column
        self.pack_propagate(False)

        # Add UI elements for the middle column here (main content, charts, etc.)
        self.stock_info_label = ctk.CTkLabel(self, text="Stock Price Graph (For 1 year)", text_color="white", font=("Roboto", 20), fg_color="#333333")
        self.stock_info_label.pack()

        self.stock_graph_frame = ctk.CTkFrame(self, fg_color="#333333")
        self.stock_graph_frame.pack(expand=True, fill='both')

        self.stock_graph_frame.grid_rowconfigure(0, weight=1)
        self.stock_graph_frame.grid_columnconfigure(0, weight=1)
        # (Add other UI elements for the middle column)


class RightColumn(ctk.CTkFrame):
    def __init__(self, parent, left_column):
        super().__init__(parent)
        self.configure(fg_color="#333333")
        self.left_column = left_column

        # Add UI elements for the right column here (watchlist, settings, etc.)
        self.watchlist_label = ctk.CTkLabel(self, text="AI News (Coming Eventually)", text_color="white", font=("Roboto", 10), fg_color="#333333")
        self.watchlist_label.pack()

        # CSV button styled the same as other buttons
        self.csvButton = ctk.CTkButton(
            self, text="View a CSV",
            fg_color="#007bff",
            text_color="white",
            font=("Roboto", 12),
            corner_radius=10,
            command=self.open_csv_finder
        )
        self.csvButton.pack(pady=10)

        response = Connection.check_internet_connection()
        if not response:
            messagebox.showwarning("No internet connection", "No internet connection")


    def open_csv_finder(self):
        self.left_column.add_stocks_csv()



if __name__ == "__main__":
    Main('Stock Viewer')
