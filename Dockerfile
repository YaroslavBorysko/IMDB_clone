FROM python:3.11
ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt-get update

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]