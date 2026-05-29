"""
Copyright (C) 2023 Flying Stocks Technologies - All Rights Reserved
www.flyingstockstechnologies.com

You cannot distribute this code under the terms of the agreement of Flying Stocks Technologies.

In case of any queries please write to:
demo@flyingstockstechnologies.com
"""

import streamlit as st
import yaml
import pandas as pd
import os
import time
import re
import requests
from database import PostgresDB
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from transformer_bridge import generate_text

def build_email_from_summary(summary):

    return f"""
Dear Customer,

We hope you are doing well.

Here is a quick update based on our recent communication:

{summary}

Please let us know if you would like to discuss further.

Regards,
CRM Team
"""

def send_email(to_email, subject, body):

    sender_email = "yourgmail@gmail.com"
    sender_password = "your_app_password"   # ⚠️ app password

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)

    except Exception as e:
        print(f"Error sending email: {e}")

# # OLLAMA FUNCTION
# def generate_summary_with_ollama(text):
#     prompt = f"""
# You are a professional text summarizer.

# Summarize the text below in exactly 3 clear and meaningful sentences.
# Do NOT repeat the original text.
# Only return the summary.

# TEXT:
# {text}
# """

#     try:
#         response = requests.post(
#              "http://host.docker.internal:11434/api/generate",
#             json={
#                 "model": "tinyllama",
#                 "prompt": prompt,
#                 "stream": False,
#                 "temperature": 0.3
#             }
#         )

#         data = response.json()

#         # 🔍 Debug print (optional)
#         print("Ollama Response:", data)

#         # ✅ Safe check
#         if "response" in data:
#             return data["response"].strip()
#         else:
#             return f"❌ Ollama Error: {data}"

#     except Exception as e:
#         return f"❌ Exception: {str(e)}"

# Transformer function 
def generate_summary_with_transformer(text):

    return generate_text(text)

# DATABASE CONFIG Load_dotenv
# DB_CONFIG = {
#     "host": "host.docker.internal",
#     "port": "5432",
#     "db": "crm",
#     "user": "postgres",
#     "password": "1234"
# }
import os

RUN_MODE = os.getenv("RUN_MODE", "local")  # default = local

if RUN_MODE == "docker":
    DB_CONFIG = {
        "host": "host.docker.internal",
        "port": "5432",
        "db": "crm",
        "user": "postgres",
        "password": "1234"
    }
else:
    DB_CONFIG = {
        "host": "localhost",
        "port": "5432",
        "db": "crm",
        "user": "postgres",
        "password": "1234"
    }


ROWS_PER_PAGE = 50

st.set_page_config(
    page_title="PostgreSQL Data Viewer",
    layout="wide"
)

st.markdown("""<style>
/* (your full styling unchanged here) */
</style>""", unsafe_allow_html=True)

st.title("📊 PostgreSQL CRM Viewer")

menu_option = "CRM View"

if "page" not in st.session_state:
    st.session_state.page = 0
if "show_data" not in st.session_state:
    st.session_state.show_data = False
if "show_form" not in st.session_state:
    st.session_state.show_form = False
if "edit_mode" not in st.session_state:
    st.session_state.edit_mode = False
if "edit_data" not in st.session_state:
    st.session_state.edit_data = None
if "confirm_delete" not in st.session_state:
    st.session_state.confirm_delete = False   
if "show_email_form" not in st.session_state:
    st.session_state.show_email_form = False     
if "generated_email" not in st.session_state:
    st.session_state.generated_email = ""
if "ai_generated" not in st.session_state:
    st.session_state.ai_generated = False
if "show_search" not in st.session_state:          
    st.session_state.show_search = False
if "search_query" not in st.session_state:         
    st.session_state.search_query = ""


with open("schema.yaml", "r") as f:
    schema = yaml.safe_load(f)

table_name = schema["table"]["name"].lower()

st.info(f"🗄️ Table: {table_name}")
st.divider()

col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])

with col_btn1:
    if st.button("📊 View Table Data"):
        st.session_state.show_data = True
        st.session_state.show_form = False
        st.session_state.edit_mode = False
        st.rerun()

with col_btn2:
    if st.button("🔍 Filter Data"):
        st.session_state.show_filter = not st.session_state.get("show_filter", False)

with col_btn3:
    if st.button("🔎 Search"):
        st.session_state.show_search = not st.session_state.show_search
        if not st.session_state.show_search:
            st.session_state.search_query = ""
        st.rerun()

if st.session_state.show_search:
    st.markdown("---")
    search_col1, search_col2 = st.columns([5, 1])

    with search_col1:
        st.session_state.search_query = st.text_input(
            label="",
            value=st.session_state.search_query,
            placeholder="🔎 Type to search CRM records...",
            label_visibility="collapsed",
            key="search_input"
        )

    with search_col2:
        if st.button("✖ Clear"):
            st.session_state.search_query = ""
            st.rerun()

    # ── YOUR SEARCH LOGIC GOES HERE LATER ──
    st.markdown("---")

try:
    db = PostgresDB(**DB_CONFIG)

    # FORM SECTION
    if st.session_state.show_form and menu_option == "CRM View":

        # 🔍 FILTER SECTION
        filters = {}

        if st.session_state.get("show_filter"):

            st.subheader("🔍 Apply Filters")

            f1, f2, f3 = st.columns(3)

            with f1:
                start_date = st.date_input("Start Date", value=None)
                end_date = st.date_input("End Date", value=None)

            with f2:
                state_filter = st.selectbox(
                    "State",
                    ["All", "Open", "Closed", "In Progress", "NQ", "Interested", "Not Interested"]
                )

            with f3:
                name_filter = st.text_input("Search Name")

            c1, c2 = st.columns(2)

            with c1:
                apply_filter = st.button("✅ Apply Filter")

            with c2:
                if st.button("❌ Clear Filter"):
                    st.session_state.show_filter = False
                    st.rerun()

        if st.session_state.edit_mode:
            st.subheader("✏️ Modify Lead")
            button_label = "✏️ Modify"
        else:
            st.subheader("📝 Add New Lead")
            button_label = "💾 Save"

        input_data = {}

        columns = [
            col for col in schema["table"]["columns"]
            if not col["name"].lower().startswith(("type", "date"))
        ]

        # 🔥 Fetch existing states from DB
        existing_states = list(set(
            [r.get("state") for r in db.fetch_table(table_name) if r.get("state")]
        ))

        for i in range(0, len(columns), 3):
            col1, col2, col3 = st.columns(3)
            group = columns[i:i+3]

            for col_ui, col_schema in zip([col1, col2, col3], group):
                col_name = col_schema["name"]
                label = col_name.replace("_", " ").title()

                default_value = ""
                if st.session_state.edit_mode and st.session_state.edit_data:
                    default_value = st.session_state.edit_data.get(col_name, "")

                with col_ui:

                    # 📝 TEXT AREA
                    if any(word in col_name.lower() for word in ["comment", "notes"]):
                        input_data[col_name] = st.text_area(label, value=default_value, height=120)

                    # 🔥 STATE DROPDOWN (DYNAMIC)
                    elif col_name.lower() == "state":

                        default_options = ["Open", "Closed", "In Progress"]
                        all_options = sorted(set(default_options + existing_states))
                        all_options.append("➕ Add New")

                        current_value = default_value if default_value else all_options[0]

                        selected = st.selectbox(
                            label,
                            all_options,
                            index=all_options.index(current_value) if current_value in all_options else len(all_options)-1,
                            key=f"{col_name}_{i}"
                        )

                        if selected == "➕ Add New":
                            custom_value = st.text_input(
                                "Enter new state",
                                value="" if current_value in all_options else current_value,
                                key=f"{col_name}_custom_{i}"
                            )
                            input_data[col_name] = (custom_value or "").strip()
                        else:
                            input_data[col_name] = selected

                    # 🔤 NORMAL INPUT
                    else:
                        input_data[col_name] = st.text_input(label, value=default_value)

        st.divider()

        col1, col2 = st.columns(2)

        with col1:
           if st.button(button_label, type="primary"):

            mobile = str(input_data.get("mobile") or "").strip()
            if not mobile.isdigit() or len(mobile) != 10:
                st.error("📱 Mobile must be 10 digits only")
                st.stop()

            email = str(input_data.get("email") or "").strip()
            pattern = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"
            if not re.match(pattern, email):
                st.error("Only valid Gmail IDs allowed")
                st.stop()

            input_data["date"] = pd.Timestamp.now()

            db.upsert_row(table_name, input_data)

            # ✅ SHOW MESSAGE
            st.success("✅ Lead Saved Successfully!")

            import time
            time.sleep(2)

            # ✅ 🔥 VERY IMPORTANT FIXES
            st.session_state.page = 0          # ← RESET TO FIRST PAGE
            st.session_state.show_data = True # ← SHOW TABLE
            st.session_state.show_filter = False

            st.session_state.show_form = False
            st.session_state.edit_mode = False
            st.session_state.edit_data = None

            st.rerun()

    # TABLE SECTION
    if st.session_state.show_data and menu_option == "CRM View":

        offset = st.session_state.page * ROWS_PER_PAGE

        # 🔍 FILTER SECTION
        start_date = None
        end_date = None
        state_filter = None
        name_filter = ""

        if st.session_state.get("show_filter"):

            st.subheader("🔍 Apply Filters")

            f1, f2, f3 = st.columns(3)

            with f1:
                start_date = st.date_input("Start Date", key="start_date")
                end_date = st.date_input("End Date", key="end_date")

            with f2:
                state_filter = st.selectbox(
                    "State",
                    ["All", "Open", "Closed", "In Progress", "NQ", "Interested", "Not Interested"],
                    key="state_filter"
                )

            with f3:
                name_filter = st.text_input("Search Name", key="name_filter")

            c1, c2 = st.columns(2)

            with c1:
                st.button("✅ Apply Filter")

            with c2:
                if st.button("❌ Clear Filter"):
                    st.session_state.show_filter = False
                    st.rerun()

        # FETCH DATA
        rows = db.fetch_table_paginated(
            table_name,
            limit=ROWS_PER_PAGE,
            offset=offset
        )

        if rows:
            df = pd.DataFrame(rows)

            # 🔥 APPLY FILTER
            if st.session_state.get("show_filter"):

                if start_date:
                    df = df[df["date"] >= pd.to_datetime(start_date)]

                if end_date:
                    df = df[df["date"] <= pd.to_datetime(end_date)]

                if state_filter and state_filter != "All":
                    df = df[df["state"] == state_filter]

                if name_filter:
                    df = df[df["name"].str.contains(name_filter, case=False, na=False)]

            # DISPLAY TABLE
            df_display = df.copy()
            df_display.index = range(offset + 1, offset + 1 + len(df_display))
            df_display.insert(0, "Select", False)

            edited_df = st.data_editor(
                df_display,
                use_container_width=True,
                key="crm_table_editor"
            )

            selected_rows = edited_df[edited_df["Select"] == True]
            selected_ids = selected_rows["email"].tolist()
            st.session_state.selected_rows = selected_rows

            # 🔥 ACTION BUTTONS (ALWAYS VISIBLE)
            col0, col1, col2, col3, col4, col5 = st.columns(6)

            # ➕ ADD NEW
            if col0.button("➕ Add New Lead"):
                st.session_state.show_form = True
                st.session_state.edit_mode = False

            # ✏️ MODIFY
            if col1.button("✏️ Modify", key="modify_btn"):
                if len(selected_rows) == 1:
                    st.session_state.edit_mode = True
                    st.session_state.edit_data = selected_rows.iloc[0].to_dict()
                    st.session_state.show_form = True
                    st.rerun()
                else:
                    st.warning("Select exactly 1 row")

                # 🗑 DELETE
            if col2.button("🗑 Delete", key="delete_btn"):
                if selected_ids:
                    st.session_state.confirm_delete = True
                else:
                    st.warning("Select rows to delete")       

            # ❌ CANCEL
            if col3.button("❌ Cancel", key="cancel_table"):
                st.rerun()

            # 🤖 SUMMARY

            if col4.button("🤖 Generate Summary"):

                if len(selected_rows) == 0:
                    st.warning("⚠️ Please select at least one row")
                    st.stop()

                progress_bar = st.progress(0)

                total_rows = len(selected_rows)

                for idx, (_, selected_row) in enumerate(selected_rows.iterrows()):

                    text = str(selected_row.get("comments", "")).strip()

                    if text:

                        summary = generate_summary_with_transformer(text)

                        db.update_summary_by_email(
                            table_name,
                            selected_row["email"],
                            summary
                        )

                    progress_bar.progress((idx + 1) / total_rows)

                st.success(f"✅ Generated summaries for {total_rows} records")

                time.sleep(1)

                st.rerun()

            
            # if col4.button("🤖 Generate Summary"):
            #     if selected_ids:
            #         for idx in selected_rows.index:
            #             real_index = idx - (offset + 1)
            #             row = rows[real_index]

            #             text = str(row.get("comments", "")).strip()
            #             if not text:
            #                 continue

            #             # summary = generate_summary_with_ollama(text)e
            #             summary = generate_summary_with_transformer(text)

            #             if "❌" not in summary:
            #                 db.update_summary_by_email(table_name, row["email"], summary)

            #         st.success("Summary generated!")

            #         st.rerun()
            #     else:
            #         st.warning("Select rows")

            # 📧 EMAIL BUTTON
            if col5.button("📧 Send Email"):

                if selected_rows.empty:
                    st.warning("⚠️ Select at least one row")
                else:
                    st.session_state.show_email_form = True
                    st.rerun()

            # 🔥 DELETE CONFIRMATION
            if st.session_state.confirm_delete:

                st.error(f"⚠️ Delete {len(selected_ids)} row(s)?")

                c1, c2 = st.columns(2)

                if c1.button("✅ Yes"):
                    db.delete_rows(table_name, selected_ids)
                    st.success("Deleted!")
                    st.session_state.confirm_delete = False
                    st.rerun()

                if c2.button("❌ No", key="cancel_delete"):
                    st.session_state.confirm_delete = False
                    st.rerun()

            # 📄 PAGINATION
            colp1, colp2 = st.columns(2)

            if colp1.button("⬅ Previous") and st.session_state.page > 0:
                st.session_state.page -= 1
                st.rerun()

            if colp2.button("Next ➡"):
                st.session_state.page += 1
                st.rerun()

    # COLUMN SUMMARY SECTION
    if menu_option == "Generate Summary":

        st.subheader("AI Column Summary Generator")

        rows = db.fetch_table(table_name)

        if rows:
            df = pd.DataFrame(rows)

            df = df.loc[:, ~df.columns.str.startswith("type")]

            selected_column = st.selectbox(
                "Select Column to Summarise",
                [col for col in df.columns if col not in ["id", "date", "summary"]]
            )

            if st.button("Generate Column Summary"):

              selected_rows = st.session_state.get("selected_rows", pd.DataFrame())

            if selected_rows.empty or len(selected_rows) != 1:
                st.warning("⚠️ Please select exactly 1 row from table")
                st.stop()

                # ✅ GET SELECTED ROW
                selected_row = selected_rows.iloc[0]

                # ✅ USE ONLY COMMENTS COLUMN
                text_to_summarize = str(selected_row["comments"]).strip()

                if not text_to_summarize:
                    st.warning("No comments available for this row")
                    st.stop()

                with st.spinner("Generating summary..."):
                    summary_text = generate_summary_with_ollama(text_to_summarize)

                    # ✅ SAVE TO DB
                    selected_email = selected_row["email"]
                    db.update_summary_by_email(table_name, selected_email, summary_text)

                    st.success("✅ Summary Generated & Saved!")
                    time.sleep(2)
                    st.write(summary_text)

                    # ✅ REFRESH TABLE
                    st.session_state.page = 0
                    st.session_state.show_data = True
                    st.rerun()

   
    # 📧 EMAIL FORM

    if st.session_state.get("show_email_form"):

        st.subheader("📧 Send Email")

        # 🔹 SUBJECT
        subject = st.text_input("Subject", key="email_subject")

        # 🔹 AI TOGGLE
        use_ai = st.toggle("🤖 Use AI")

        # =========================
        # 🤖 AI MODE
        # =========================
        if use_ai:

            prompt = st.text_area("Enter Prompt for AI")

            # 🚫 Disabled until AI generates
            message = st.text_area(
                "Message",
                value=st.session_state.generated_email,
                disabled=not st.session_state.ai_generated,
                height=200
            )

            if st.button("🤖 Generate Email"):

                if not prompt.strip():
                    st.warning("Please enter a prompt")
                    st.stop()

                with st.spinner("Generating..."):

                    try:
                        # response = requests.post(
                        #     "http://host.docker.internal:11434/api/generate",
                        #     json={
                        #         "model": "tinyllama",
                        #         "prompt": prompt,
                        #         "stream": False
                        #     },
                        #     timeout=180
                        # )

                        # data = response.json()
                        # generated = data.get("response", "").strip()

                        # generated = generate_text(prompt)
                        summary = generate_summary_with_transformer(prompt)
                        generated = build_email_from_summary(summary)

                        
                        # remove unwanted Subject
                        if generated.lower().startswith("subject"):
                            generated = "\n".join(generated.split("\n")[1:]).strip()

                        st.session_state.generated_email = generated
                        st.session_state.ai_generated = True
                        st.rerun()
                        

                        # remove unwanted Subject
                        if generated.lower().startswith("subject"):
                            generated = "\n".join(generated.split("\n")[1:]).strip()

                        st.session_state.generated_email = generated
                        st.session_state.ai_generated = True

                        st.rerun()

                    except Exception as e:
                        st.error(f"Error: {e}")

        # =========================
        # ✍️ MANUAL MODE
        # =========================
        else:
            st.session_state.ai_generated = False

            message = st.text_area(
                "Message",
                height=200
            )

        # 🔹 SEND + EXIT
        col1, col2 = st.columns(2)

        if col1.button("📨 Send Now"):

            selected_rows = st.session_state.get("selected_rows", pd.DataFrame())

            if selected_rows.empty:
                st.warning("⚠️ No recipients selected")
                st.stop()

            for _, row in selected_rows.iterrows():
                personalized_msg = f"""
    Hi {row.get('name', '')},

    {message}

    Regards,
    CRM Team
    """
                send_email(row["email"], subject, personalized_msg)

            st.success(f"✅ Email sent to {len(selected_rows)} users")

            st.session_state.show_email_form = False
            st.session_state.generated_email = ""
            st.session_state.ai_generated = False

            st.rerun()

        if col2.button("❌ Exit"):
            st.session_state.show_email_form = False
            st.session_state.generated_email = ""
            st.session_state.ai_generated = False
            st.rerun()

except Exception as e:
    st.error("❌ Database connection error")
    st.exception(e)

