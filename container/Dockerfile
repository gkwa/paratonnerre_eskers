FROM python:3-slim-bullseye

RUN mkdir -p /src
COPY requirements.txt /src
RUN pip install --upgrade pip --requirement /src/requirements.txt
COPY run.py /src
COPY run.sh /src

WORKDIR /src

ENTRYPOINT ["./run.sh"]
