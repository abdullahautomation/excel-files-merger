import pandas as pd
import os

os.makedirs("excel_files", exist_ok=True)

january_data = {
    "Name": ["Ali", "Sara", "Ahmed"],
    "Sales": [5000, 7000, 4500],
    "Month": ["January", "January", "January"]
}

february_data = {
    "Name": ["Ali", "Sara", "Ahmed"],
    "Sales": [6000, 8000, 5000],
    "Month": ["February", "February", "February"]
}

march_data = {
    "Name": ["Ali", "Sara", "Ahmed"],
    "Sales": [7000, 9000, 6000],
    "Month": ["March", "March", "March"]
}

pd.DataFrame(january_data).to_excel("excel_files/January.xlsx", index=False)
pd.DataFrame(february_data).to_excel("excel_files/February.xlsx", index=False)
pd.DataFrame(march_data).to_excel("excel_files/March.xlsx", index=False)

print("Files ban gayi!")