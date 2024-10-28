FROM python:3.11-buster

RUN apt-get update -y
RUN apt-get install -y \
  python3-pip \
  python3-venv \
  build-essential \
  libpq-dev \
  libmariadbclient-dev \
  zlib1g-dev \
  libwebp-dev \
  curl  \
  vim \
  net-tools

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

ADD . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]