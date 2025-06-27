# Базовый образ с Python (можно заменить на нужную версию)
FROM python:3.12-slim

# Устанавливаем переменные окружения (не буферизуем вывод, удобно для логов)
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё остальное в контейнер
COPY . .

# Открываем порт (опционально, для инфы)
EXPOSE 8000

# Команда запуска приложения по умолчанию
# Можно заменить на ["python", "manage.py", "runserver", "0.0.0.0:8000"] — для Django
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
