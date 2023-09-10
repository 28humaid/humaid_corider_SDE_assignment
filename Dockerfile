FROM python:3.9

WORKDIR /humaid_corider_SDE_assignment

COPY app.py .
COPY requirements.txt .
COPY api_end_points/ ./api_end_points/

RUN pip install -r requirements.txt


ENV MONGO_URI mongodb://mongo:27017/user_db

CMD ["flask", "run", "--host=0.0.0.0"]
