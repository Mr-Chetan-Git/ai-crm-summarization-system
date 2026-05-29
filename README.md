# CRM AI Lead Management System

## Overview

CRM AI Lead Management System is a Streamlit-based application integrated with PostgreSQL and a custom Transformer model for customer follow-up summarization.

The system helps sales and business teams manage leads, track follow-ups, generate AI summaries, and send emails efficiently.

## Features

### CRM Management

* Add new leads
* Modify existing leads
* Delete leads
* Search and filter records
* View customer follow-up history
* Export CRM data

### AI Summarization

Generate concise summaries from long customer interaction histories.

Example:

#### Comments

```text
19 May - Busy
18 May - No response
16 May - No response
15 May - Syllabus walkthrough
```

#### Generated Summary

```text
Customer attended the syllabus walkthrough but remained unavailable afterward.
Repeated follow-ups received limited responses due to scheduling conflicts.
```

### Bulk Summary Generation

* Select multiple leads
* Generate summaries in one click
* Automatically save summaries to the database

### Email Module

* Send emails to leads
* Generate AI-assisted content
* Personalized communication

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Database

* PostgreSQL

### AI and Machine Learning

* Custom Transformer Model
* PyTorch

### Data Processing

* Pandas
* NumPy

### Deployment

* Docker

## Project Structure

```text
CRM/
│
├── .vscode/
├── __pycache__/
├── checkpoints/
│
├── transformer/
│   └── Transformer-main/
│       ├── run_project.py
│       ├── config.py
│       ├── tasks/
│       ├── models/
│       ├── utils/
│       ├── checkpoints/
│       └── datasets/
│
├── venv/
│
├── .env
├── backup.sql
├── crm_app.tar
├── crm_export.csv
│
├── CRM_UI.py
├── database.py
├── loader.py
├── transformer_bridge.py
├── export_db_to_excel.py
│
├── Dockerfile
├── requirements.txt
├── schema.yaml
├── license.key
│
└── README.md
```

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd CRM
```

### Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux or Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Database Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE crm;
```

Configure the database connection in your application settings.

Example:

```python
DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "database": "crm",
    "user": "postgres",
    "password": "your_password"
}
```

## Running the CRM Application

```bash
streamlit run CRM_UI.py
```

The application will be available at:

```text
http://localhost:8501
```

## Transformer Model

Location:

```text
transformer/Transformer-main/
```

Responsibilities:

* Train summarization model
* Generate CRM summaries
* Learn patterns from customer interactions

## Training Data Format

Example:

```python
SUMMARIZATION_DATA = [
    (
        "customer busy and not answering calls",
        "Customer remained unavailable because of busy schedules."
    ),
    (
        "customer requested syllabus and demo video",
        "Customer showed interest and requested course information."
    )
]
```

## Model Training

Run the training process:

```bash
python transformer/Transformer-main/run_project.py --task summarization --save-checkpoint
```

Checkpoint files will be stored inside:

```text
checkpoints/
```

## Summary Generation Workflow

```text
Customer Comments
        │
        ▼
Transformer Model
        │
        ▼
Generated Summary
        │
        ▼
PostgreSQL Database
        │
        ▼
CRM Dashboard
```

## Export Data

```bash
python export_db_to_excel.py
```

Output:

```text
crm_export.csv
```

## Docker Support

Build Docker image:

```bash
docker build -t crm-ai .
```

Run Docker container:

```bash
docker run -p 8501:8501 crm-ai
```

## Future Enhancements

* Improved Transformer Summarization
* Lead Scoring
* Email Campaign Automation
* Dashboard Analytics
* Multi-language Support
* LLM Integration
* Customer Intent Detection

## Author

Chetan S

CRM AI Lead Management System built using:

* Streamlit
* PostgreSQL
* PyTorch
* Custom Transformer Architecture

## License

This project is intended for educational and internal CRM automation purposes.
