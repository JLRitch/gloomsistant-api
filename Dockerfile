FROM python:3.9-slim

WORKDIR /usr

COPY requirements.txt ./
COPY requirements-dev.txt ./
COPY requirements.sh ./

ARG PY_ENV=prod
ENV PY_ENV=$PY_ENV

RUN bash requirements.sh

RUN mkdir -p /src
COPY ./src /usr/src
WORKDIR /usr/src

EXPOSE 8000

# initialize a dev database !!!!REMOVE BEFORE TEST/PROD!!!!
RUN python3 -m db.initialize

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# GROWTH, enable live reload
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload-dir", "./models", "--reload-dir", "./routes", "--reload-dir", "./test"]