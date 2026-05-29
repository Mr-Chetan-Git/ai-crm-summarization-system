"""
Copyright (C) 2023 Flying Stocks Technologies - All Rights Reserved
www.flyingstockstechnologies.com

You cannot distribute this code under the terms of the agreement of Flying Stocks Technologies.

In case of any queries please write to:
demo@flyingstockstechnologies.com
"""

# loader.py
import yaml
import pandas as pd
from database import PostgresDB
import os
from sqlalchemy import text  # ✅ Added for safe DELETE execution


# DATABASE CONFIG
DB_CONFIG = {
    "host": "host.docker.internal",
    "port": "5432",
    "db": "crm",
    "user": "postgres",
    "password": "1234"
}


def detect_header_row(path, max_rows=15):
    preview = pd.read_excel(path, header=None, nrows=max_rows)
    for i in range(len(preview)):
        row = preview.iloc[i].astype(str).str.lower()
        if {"date", "name", "email"}.issubset(set(row)):
            return i
    return 0


def clean_row_for_db(row, schema_types):
    """
    Convert NaT to None, truncate strings for varchar(255)
    """
    clean_row = {}
    for col, dtype in schema_types.items():
        value = row.get(col)

        if pd.isna(value):
            value = None

        if dtype.lower() in ["varchar", "character varying"] and isinstance(value, str):
            value = value[:255]

        clean_row[col] = value

    return clean_row


def load_excel_to_postgres():
    # LOAD SCHEMA
    with open("schema.yaml", "r") as f:
        schema = yaml.safe_load(f)

    excel_filepath_to_load_data = schema["excel_filepath_to_load_data"]["path"]
    table_name = schema["table"]["name"].lower()
    columns = schema["table"]["columns"]
    schema_types = {c["name"].lower(): c["type"] for c in columns}

    db = PostgresDB(**DB_CONFIG)

    # CREATE / SYNC TABLE
    db.create_table_if_not_exists(table_name, schema_types)

    # 🔥 CLEAR OLD DATA (Fresh Load Every Time)
    with db.engine.begin() as conn:
        conn.execute(text(f"DELETE FROM {table_name}"))

    if not os.path.exists(excel_filepath_to_load_data):
        raise FileNotFoundError(f"The file {excel_filepath_to_load_data} does not exist.")

    # READ EXCEL
    header_row = detect_header_row(excel_filepath_to_load_data)
    df = pd.read_excel(excel_filepath_to_load_data, header=header_row)

    # CLEAN COLUMNS
    df = df.loc[:, ~df.columns.astype(str).str.contains("^unnamed", case=False)]
    df.columns = df.columns.astype(str).str.strip().str.lower().str.replace(" ", "_")

    # ALIGN TO SCHEMA
    for col in schema_types:
        if col not in df.columns:
            df[col] = None

    df = df[list(schema_types.keys())]

    # CONVERT DATETIME SAFELY
    for col, t in schema_types.items():
        if t.lower() == "datetime":
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # INSERT ROW-BY-ROW
    inserted = 0
    for _, row in df.iterrows():
        row_dict = clean_row_for_db(row.to_dict(), schema_types)

        # 🔥 FIX MOBILE NUMBER (Excel scientific notation issue)
        if "mobile" in row_dict and row_dict["mobile"] is not None:
            val = str(row_dict["mobile"])
            if "E" in val:
                try:
                    val = format(float(val), '.0f')
                except:
                    pass
            row_dict["mobile"] = val.strip()

        # 🔥 SKIP EMPTY EMAIL (important)
        if not row_dict.get("email"):
            continue

        try:
            db.upsert_row(table_name, row_dict)
            inserted += 1
        except Exception as e:
            print(f"❌ Error inserting row {row_dict.get('email')}: {e}")

    return inserted, table_name, f"✅ Inserted {inserted} rows (Fresh load - old data cleared)"


# EXPORT FUNCTION (CSV VERSION)
def export_table_to_csv(output_path="crm_export.csv", limit=None):
    with open("schema.yaml", "r") as f:
        schema = yaml.safe_load(f)

    table_name = schema["table"]["name"].lower()
    db = PostgresDB(**DB_CONFIG)

    rows = db.fetch_table(table_name, limit)

    if not rows:
        return None

    df = pd.DataFrame(rows)

    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    df.to_csv(output_path, index=False)

    return output_path


if __name__ == "__main__":
    rows, table, message = load_excel_to_postgres()
    print(message)
    export_table_to_csv()