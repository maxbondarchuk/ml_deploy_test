FROM python:3.10-slim

COPY *.py /app/
COPY *.csv /app/
COPY requirements.txt /app/

WORKDIR /app/

RUN pip install -r requirements.txt

RUN python train.py

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]