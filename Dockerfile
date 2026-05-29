FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install torch torchvision torchaudio

EXPOSE 8501

CMD ["streamlit", "run", "CRM_UI.py", "--server.port=8501", "--server.address=0.0.0.0"]
