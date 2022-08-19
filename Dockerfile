FROM python:3-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

VOLUME ["/data"]

CMD ["python", "main.py"]