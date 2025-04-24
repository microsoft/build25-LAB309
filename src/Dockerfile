FROM python:3.11

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT ["gunicorn", "-c", "gunicorn.conf.py", "app:app"]
