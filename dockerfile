FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --upgrade pip setuptools wheel \
    && pip install scikit-learn==1.7.1 \
    && pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
