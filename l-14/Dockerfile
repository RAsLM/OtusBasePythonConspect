FROM python:3.9-bullseye

WORKDIR /var/app

CMD pip install virtualenv \
    virtualenv venv \
    source venv/bin/activate

RUN pwd && ls -la

COPY blog/requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY blog .



CMD uvicorn app:app --host=0.0.0.0







