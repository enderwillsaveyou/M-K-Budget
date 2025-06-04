import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import openpyxl

class EditableTable(tk.Frame):
    """Simple table widget with editable cells using Entry widgets."""
    def __init__(self, master, headers, data=None, **kwargs):
        super().__init__(master, **kwargs)
        self.headers = headers
        self.data = data or []
        self.entries = []  # list of rows; each row is list of Entry widgets
        self._build_table()

    def _build_table(self):
        # create header labels
        for col, header in enumerate(self.headers):
            label = tk.Label(self, text=header, font=("Arial", 10, "bold"))
            label.grid(row=0, column=col, padx=2, pady=2)

        for row_idx, row_data in enumerate(self.data, start=1):
            self.add_row(row_data)

    def add_row(self, row_data=None):
        row_data = row_data or ["" for _ in self.headers]
        row_entries = []
        row_idx = len(self.entries) + 1
        for col_idx, value in enumerate(row_data):
            e = tk.Entry(self)
            e.insert(0, value)
            e.grid(row=row_idx, column=col_idx, padx=2, pady=2)
            row_entries.append(e)
        self.entries.append(row_entries)

    def get_data(self):
        result = []
        for row_entries in self.entries:
            result.append([e.get() for e in row_entries])
        return result


class BudgetApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Family Budget App")

        # Credit Card Section
        cc_frame = tk.LabelFrame(self, text="Credit Cards")
        cc_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        cc_headers = ["Card Name", "Total", "Credit Limit", "Minimum Payment", "Interest Rate"]
        cc_data = [
            ["Discover", "0", "25000", "0", "0.13"],
            ["LOC", "0", "35000", "0", ""],
            ["Amazon", "0", "0", "100", ""],
        ]
        self.cc_table = EditableTable(cc_frame, cc_headers, cc_data)
        self.cc_table.pack()

        # Savings Section
        sav_frame = tk.LabelFrame(self, text="Savings Accounts")
        sav_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        sav_headers = ["Account", "Balance"]
        sav_data = [
            ["Retirement savings", "30000"],
            ["401K's (Approx)", ""],
            ["Joe", "100000"],
        ]
        self.sav_table = EditableTable(sav_frame, sav_headers, sav_data)
        self.sav_table.pack()

        export_btn = tk.Button(self, text="Export to Excel", command=self.export_to_excel)
        export_btn.pack(pady=10)

    def export_to_excel(self):
        # gather data
        cc_data = self.cc_table.get_data()
        sav_data = self.sav_table.get_data()

        file_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx")],
            title="Save as"
        )
        if not file_path:
            return

        wb = openpyxl.Workbook()
        ws_cc = wb.active
        ws_cc.title = "Credit Cards"
        ws_cc.append(self.cc_table.headers)
        for row in cc_data:
            ws_cc.append(row)

        ws_sav = wb.create_sheet(title="Savings")
        ws_sav.append(self.sav_table.headers)
        for row in sav_data:
            ws_sav.append(row)

        wb.save(file_path)


def main():
    app = BudgetApp()
    app.mainloop()

if __name__ == "__main__":
    main()
