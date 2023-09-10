FROM python:3.9

WORKDIR /app

COPY app.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP app.py
ENV FLASK_ENV production
ENV FLASK_DEBUG 0
ENV MONGO_URI mongodb://mongo:27017/user_db

CMD ["flask", "run", "--host=0.0.0.0"]
