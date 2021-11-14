FROM python:3.9-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt ./

RUN ls

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8000

# initialize a dev database !!!!REMOVE BEFORE TEST/PROD!!!!
RUN python3 -m db.initialize

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]