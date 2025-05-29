FROM python:3.12-slim

WORKDIR /app

COPY . /backend

RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt


    CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && \
    python create_superuser.py && uvicorn mysite.asgi:application --workers 5 --host 0.0.0.0 --port 8000" ]