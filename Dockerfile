FROM python:3.6-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080 8000

# initialize a dev database !!!!REMOVE BEFORE TEST/PROD!!!!
RUN python -m db.initialize

ENTRYPOINT ["uvicorn"]

CMD ["main:app"]