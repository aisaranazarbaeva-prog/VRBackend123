# Используем официальный Python образ
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Собираем статические файлы (если нужны)
RUN python manage.py collectstatic --noinput || true

# Применяем миграции
RUN python manage.py makemigrations || true
RUN python manage.py migrate || true
RUN python manage.py runserver || true


# Открываем порт
EXPOSE 8000

# Запускаем сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
