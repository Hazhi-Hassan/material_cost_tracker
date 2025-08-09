import tkinter as tk
from tkinter import ttk, messagebox
from db import Database
from excel_export.py import export_boq

db = Database("materials.db")

class MaterialCostApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Material Cost Tracker")
        self.geometry("900x600")

        # Placeholder for logo/company info
        logo_frame = tk.Frame(self, height=80, bg="white")
        logo_frame.pack(fill="x")
        tk.Label(logo_frame, text="Your Company Name", font=("Arial", 16, "bold"), bg="white").pack()

        # Tabs
        tab_control = ttk.Notebook(self)
        self.item_tab = ttk.Frame(tab_control)
        self.boq_tab = ttk.Frame(tab_control)
        tab_control.add(self.item_tab, text="Items")
        tab_control.add(self.boq_tab, text="Bill of Quantities")
        tab_control.pack(expand=1, fill="both")

        self.setup_items_tab()
        self.setup_boq_tab()

    def setup_items_tab(self):
        # Table
        columns = ("name", "date", "price", "unit", "description", "seller", "location", "phone")
        self.item_tree = ttk.Treeview(self.item_tab, columns=columns, show="headings")
        for col in columns:
            self.item_tree.heading(col, text=col.capitalize())
        self.item_tree.pack(expand=True, fill="both")
        self.load_items()

        # Buttons
        btn_frame = tk.Frame(self.item_tab)
        btn_frame.pack()
        tk.Button(btn_frame, text="Add Item", command=self.add_item).pack(side="left")
        tk.Button(btn_frame, text="Edit Item", command=self.edit_item).pack(side="left")
        tk.Button(btn_frame, text="Delete Item", command=self.delete_item).pack(side="left")

    def load_items(self):
        for row in self.item_tree.get_children():
            self.item_tree.delete(row)
        for item in db.get_all_items():
            self.item_tree.insert("", "end", values=item)

    def add_item(self):
        messagebox.showinfo("Add", "Implement add item form")

    def edit_item(self):
        messagebox.showinfo("Edit", "Implement edit item form")

    def delete_item(self):
        messagebox.showinfo("Delete", "Implement delete item logic")

    def setup_boq_tab(self):
        tk.Label(self.boq_tab, text="Create and Export Bill of Quantities").pack()
        tk.Button(self.boq_tab, text="Export BOQ to Excel", command=self.export_boq).pack()

    def export_boq(self):
        export_boq(db, "assets/template_bo.xlsx")
        messagebox.showinfo("Export", "BOQ exported successfully!")

if __name__ == "__main__":
    app = MaterialCostApp()
    app.mainloop()
