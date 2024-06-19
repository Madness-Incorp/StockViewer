import tkinter as tk
import customtkinter as ctk
import Helpers as hp


class Main(ctk.CTk):

    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.geometry('800x600')

        # Create frame objects for each column
        self.left_column = LeftColumn(self)
        self.middle_column = MiddleColumn(self)
        self.right_column = RightColumn(self)

        # Add frames to the grid layout
        self.left_column.grid(row=0, column=0, sticky="nsew")
        self.middle_column.grid(row=0, column=1, sticky="nsew")
        self.right_column.grid(row=0, column=2, sticky="nsew")

        # Configure column weights for balanced layout (adjust as needed)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)

        self.mainloop()


class LeftColumn(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        # Add UI elements for the left column here (buttons, labels, etc.)
        self.navigation_label = ctk.CTkLabel(self, text="Navigation", fg_color='grey', bg_color= 'grey')
        self.navigation_label.pack()

        self.adder_button = ctk.CTkButton(self, text="+", bg_color='grey', fg_color='grey', text_color='green', width=10, height=10, corner_radius=10, command=hp.create_window)
        self.adder_button.pack(side = 'right')

        # (Add other UI elements for the left column)
        
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
        self.watchlist_label = ctk.CTkLabel(self, text="Watchlist")
        self.watchlist_label.pack()

        # (Add other UI elements for the right column)




if __name__ == "__main__":
    Main('Stock Viewer')
