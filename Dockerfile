FROM python:3.12.9-slim

USER root

RUN apt-get update && apt-get install -y sqlite3 vim

RUN useradd --create-home python

USER python

WORKDIR /home/python/app

COPY --chown=python:python requirements.txt .

RUN pip install --upgrade pip

RUN pip install --user --no-cache-dir --upgrade -r requirements.txt

ENV PATH="/home/python/.local/bin:${PATH}"

COPY --chown=python:python . .

RUN find /home/python/app -name "__pycache__" -type d -exec rm -rf {} +

CMD ["python", "app/run.py", "--host=0.0.0.0"]

EXPOSE 5000