FROM python:3.12

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

WORKDIR /app

COPY ./notebook.py notebook.py
COPY ./yellow_tripdata_2021-01.csv yellow_tripdata_2021-01.csv

ENTRYPOINT [ "python", "notebook.py" ]
