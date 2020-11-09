FROM python:3.8-alpine

COPY ./app.py /app/app.py
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

CMD gunicorn \
    --access-logfile - \
    --error-logfile - \
    --worker-tmp-dir /dev/shm \
    --workers 2 \
    --threads 4 \
    --worker-class gthread \
    --bind 0.0.0.0:5000 \
    app:app