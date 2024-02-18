FROM python:3.10.13-slim-bullseye

WORKDIR /app

COPY . /app

RUN apt update && apt-get install ffmpeg -y

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["streamlit", "run", "analyze.py", "--server.port", "8501"]