FROM python:3.12

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY app/main.py ./main.py

EXPOSE 5000

CMD ["python", "main.py"]