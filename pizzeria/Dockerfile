
FROM python:3.9




RUN mkdir /app
COPY . /app
WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update && apt-get install -y pkg-config libmariadb-dev gcc

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt




EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
