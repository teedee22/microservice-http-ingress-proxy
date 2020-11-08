FROM python:3.8-alpine

COPY ./app.py /app/app.py
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]