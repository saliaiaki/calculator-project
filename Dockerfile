# Берём образ с Python
FROM python:3.11-slim

# Создаём папку внутри контейнера
WORKDIR /app

# Копируем наши файлы в контейнер
COPY calc.py style.py ./

# Говорим, как запускать
CMD ["python3", "calc.py"]