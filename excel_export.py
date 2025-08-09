import pandas as pd

def export_boq(db, template_path):
    items = db.get_all_items()
    df = pd.DataFrame(items, columns=["Name", "Date Added", "Price", "Unit", "Description", "Seller Name", "Shop Location", "Phone"])
    writer = pd.ExcelWriter("boq_export.xlsx", engine="openpyxl")
    df.to_excel(writer, index=False, startrow=5)  # leave space for logo
    writer.save()
