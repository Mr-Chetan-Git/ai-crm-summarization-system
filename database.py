"""
Copyright (C) 2023 Flying Stocks Technologies - All Rights Reserved
www.flyingstockstechnologies.com

You cannot distribute this code under the terms of the agreement of Flying Stocks Technologies.

In case of any queries please write to:
demo@flyingstockstechnologies.com
"""

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import create_engine, Table, Column, MetaData, select
from sqlalchemy.dialects.postgresql import VARCHAR, TEXT, TIMESTAMP, BIGINT
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

class PostgresDB:
    def __init__(self, host, port, db, user, password):
        self.engine = create_engine(
            f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}",
            future=True
        )
        self.metadata = MetaData()      

    def create_table_if_not_exists(self, table_name, schema_types):
        columns = []

        for col, dtype in schema_types.items():
            t = dtype.lower()

            if t == "datetime":
                columns.append(Column(col, TIMESTAMP))
            elif t == "bigint":
                columns.append(Column(col, BIGINT))
            else:
                if any(k in col for k in ["notes", "comments", "youtube", "gap", "type", "summary"]):
                    columns.append(Column(col, TEXT))
                else:
                    columns.append(Column(col, VARCHAR(255)))

        # Email UNIQUE constraint added here
        table = Table(
            table_name,
            self.metadata,
            *columns,
            extend_existing=True
        )

        self.metadata.create_all(self.engine)

        # Ensure UNIQUE constraint exists
        with self.engine.begin() as conn:
            conn.execute(text(f"""
                        DO $$
                        BEGIN
                            IF NOT EXISTS (
                                SELECT 1 FROM pg_constraint
                                WHERE conname = '{table_name}_email_unique'
                            ) THEN
                                ALTER TABLE {table_name}
                                ADD CONSTRAINT {table_name}_email_unique UNIQUE (email);
                            END IF;
                        END $$;
                        """))
        return table
 
    def insert_row(self, table_name, row_dict):
        table = Table(table_name, self.metadata, autoload_with=self.engine)
        with self.engine.begin() as conn:
            conn.execute(table.insert().values(**row_dict))

    def fetch_existing_keys(self, table_name, key_column):
        table = Table(table_name, self.metadata, autoload_with=self.engine)
        with self.engine.connect() as conn:
            result = conn.execute(select(table.c[key_column]))
            return [r[0] for r in result if r[0] is not None]

    def fetch_table(self, table_name, limit=None):
        table = Table(table_name, self.metadata, autoload_with=self.engine)
        stmt = select(table)
        if limit:
            stmt = stmt.limit(limit)

        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            return [dict(row._mapping) for row in result]
        
    def fetch_table_paginated(self, table_name, limit=50, offset=0):
        table = Table(table_name, self.metadata, autoload_with=self.engine)

        # Order by latest ID first
        stmt = select(table).order_by(table.c.date.desc()).limit(limit).offset(offset)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
        return [dict(row._mapping) for row in result]
        
    def upsert_row(self, table_name, row_dict, conflict_column="email"):
        table = Table(table_name, self.metadata, autoload_with=self.engine)
        insert_stmt = insert(table).values(**row_dict)

        # Update all columns EXCEPT email
        update_columns = {
            col: row_dict[col]
            for col in row_dict
            if col != conflict_column
        }

        upsert_stmt = insert_stmt.on_conflict_do_update(
            index_elements=[conflict_column],
            set_=update_columns
        )

        with self.engine.begin() as conn:
            conn.execute(upsert_stmt)

    # ✅ ADDED THIS FUNCTION ONLY
    def update_row(self, table_name, row_id, data):
        table = Table(table_name, self.metadata, autoload_with=self.engine)

        stmt = (
            table.update()
            .where(table.c.email == row_id)
            .values(**data)
        )

        with self.engine.begin() as conn:
            conn.execute(stmt)

    # FOR DELETING THE ROWS 
    def delete_rows(self, table_name, ids):
        table = Table(table_name, self.metadata, autoload_with=self.engine)

        with self.engine.begin() as conn:
            conn.execute(
            table.delete().where(table.c.email.in_(ids))
            )

    def update_summary_by_email(self, table_name, email, summary):
         with self.engine.begin() as conn:
            conn.execute(
            text(f"""
                UPDATE {table_name}
                SET summary = :summary
                WHERE email = :email
            """),
            {"summary": summary, "email": email}
        )       