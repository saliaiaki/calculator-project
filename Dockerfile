FROM python:3.11-slim

WORKDIR /app

COPY calc.py style.py ./

# Устанавливаем зависимости
RUN pip install psycopg2-binary

CMD ["python3", "calc.py"]