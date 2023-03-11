FROM python:3.9



COPY ./requirements.txt /home/ubuntu/projects/fastApi-example/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /home/ubuntu/projects/fastApi-example/requirements.txt

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]