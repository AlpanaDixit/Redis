FROM python:3
ENV PYTHONUNBUFFERED=1 
WORKDIR /user/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt