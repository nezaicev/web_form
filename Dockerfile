FROM python:3.9.6-alpine

RUN apk update && apk add bash

RUN mkdir -p  /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

RUN chmod a+x ./run.sh


ENTRYPOINT ["./run.sh"]