FROM python:3.9

WORKDIR /code

COPY ./app /code/app
COPY requirements.txt /code/

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
