"""
Copyright (C) 2023 Flying Stocks Technologies - All Rights Reserved
www.flyingstockstechnologies.com

You cannot distribute this code under the terms of the agreement of Flying Stocks Technologies.

In case of any queries please write to:
demo@flyingstockstechnologies.com
"""
import pandas as pd
import yaml
from database import PostgresDB
import os

DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "db": "crm",
    "user": "postgres",
    "password": "1234"
}

def export_table_to_excel():
    with open("schema.yaml", "r") as f:
        schema = yaml.safe_load(f)

    if not schema.get("export", {}).get("enabled", False):
        print("❌ Export disabled in schema.yaml")
        return

    output_path = schema["export"]["output_path"]
    table_name = schema["table"]["name"].lower()

    db = PostgresDB(**DB_CONFIG)

    rows = db.fetch_table(table_name, limit=100000)

    if not rows:
        print("⚠️ No data found in database")
        return

    df = pd.DataFrame(rows)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_excel(output_path, index=False)

    print(f"✅ Data exported to Excel: {output_path}")

if __name__ == "__main__":
    export_table_to_excel()