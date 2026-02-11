FROM python:3.12

RUN pip install pandas pyarrow

WORKDIR /app

COPY ./ingest_data.py ingest_data.py

ENTRYPOINT [ "python", "ingest_data.py" ]
