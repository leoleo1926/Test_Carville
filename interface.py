from functions import calc_prices
import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        input_price = float(input_entry.get())
        nds_percent = int(nds_entry.get())
        price_with_nds, price_without_nds = calc_prices(input_price, nds_percent)
        result_label.config(text=f"Price with NDS: {price_with_nds:.2f}\nPrice without NDS: {price_without_nds:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a number.")

root = tk.Tk()
root.title("Price Calculator")


main_frame = ttk.Frame(root, padding=20, style="PersicFrame.TFrame")
main_frame.grid(row=0, column=0, sticky="nsew")

style = ttk.Style()
style.configure("PersicFrame.TFrame", background="#FFCDD2") 

input_label = ttk.Label(main_frame, text="Input Price with NDS:")
input_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

input_entry = ttk.Entry(main_frame)
input_entry.grid(row=0, column=1, sticky="w", padx=10, pady=10)

nds_label = ttk.Label(main_frame, text="NDS (%):")
nds_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

nds_entry = ttk.Entry(main_frame)
nds_entry.grid(row=1, column=1, sticky="w", padx=10, pady=10)


calculate_button = ttk.Button(main_frame, text="Calculate", command=calculate)
calculate_button.grid(row=2, column=0, columnspan=2, pady=20)


result_label = ttk.Label(main_frame, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
