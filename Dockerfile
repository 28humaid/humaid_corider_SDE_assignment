FROM python:3.9

WORKDIR /humaid_corider_SDE_assignment

COPY app.py .
COPY requirements.txt .
COPY api_end_points/ ./api_end_points/

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP app.py
ENV FLASK_ENV production
ENV FLASK_DEBUG 0
ENV MONGO_URI mongodb://mongo:27017/user_db

CMD ["flask", "run", "--host=0.0.0.0"]
