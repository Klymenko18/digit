# Використовуємо базовий образ Python
FROM python:3.12-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файл залежностей
COPY requirements.txt /app/

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо решту коду проекту
COPY . /app/

# Відкриваємо порт
EXPOSE 8000

# Команда для запуску сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
