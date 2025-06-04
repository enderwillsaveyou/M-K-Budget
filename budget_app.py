import tkinter as tk
from tkinter import ttk

class BudgetApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Family Budget App")
        self.geometry("400x400")
        self._create_widgets()

    def _create_widgets(self):
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Income
        ttk.Label(main_frame, text="Monthly Income:").grid(row=0, column=0, sticky=tk.W)
        self.income_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.income_var).grid(row=0, column=1, pady=5)

        # House expense
        ttk.Label(main_frame, text="House Payment:").grid(row=1, column=0, sticky=tk.W)
        self.house_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.house_var).grid(row=1, column=1, pady=5)

        # Car expense
        ttk.Label(main_frame, text="Car Payment:").grid(row=2, column=0, sticky=tk.W)
        self.car_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.car_var).grid(row=2, column=1, pady=5)

        # Bills expense
        ttk.Label(main_frame, text="Monthly Bills:").grid(row=3, column=0, sticky=tk.W)
        self.bills_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.bills_var).grid(row=3, column=1, pady=5)

        # Summary
        self.summary_var = tk.StringVar()
        ttk.Label(main_frame, textvariable=self.summary_var, foreground="blue").grid(row=5, column=0, columnspan=2, pady=10)

        # Calculate button
        ttk.Button(main_frame, text="Calculate", command=self.calculate).grid(row=4, column=0, columnspan=2, pady=10)

        for child in main_frame.winfo_children():
            child.grid_configure(padx=5)

    def calculate(self):
        try:
            income = float(self.income_var.get())
            house = float(self.house_var.get())
            car = float(self.car_var.get())
            bills = float(self.bills_var.get())
        except ValueError:
            self.summary_var.set("Please enter valid numbers.")
            return

        total_expenses = house + car + bills
        balance = income - total_expenses
        self.summary_var.set(f"Monthly balance: ${balance:.2f}")

if __name__ == "__main__":
    app = BudgetApp()
    app.mainloop()

