FROM python:3.13-slim-bullseye

RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    build-essential \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && pip install --no-cache-dir --upgrade pip \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --requirement /app/requirements.txt
COPY . /app

EXPOSE 5000

CMD [ "python3", "server.py" ]