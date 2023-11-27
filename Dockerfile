FROM python:3.10-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./3.2-crud/stocks_products/requirements.txt /usr/src/app
RUN pip3 install -r requirements.txt

COPY . /usr/src/app

EXPOSE 8000

CMD ["python3", "/usr/src/app/3.2-crud/stocks_products/manage.py", "runserver", "0.0.0.0:8000"]
