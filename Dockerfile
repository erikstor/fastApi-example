FROM python:3.9

WORKDIR /home/ubuntu/projects/fastApi-example

COPY ./requirements.txt /home/ubuntu/projects/fastApi-example/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /home/ubuntu/projects/fastApi-example/app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]