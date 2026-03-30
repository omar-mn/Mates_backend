FROM python:3.12.3
WORKDIR /mates_backend
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD [ "python" , "manage.py" , "runserver" ]ٍ