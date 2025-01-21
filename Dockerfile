FROM python:3.10-slim

WORKDIR /agent
COPY . /agent

RUN pip install fastapi uvicorn

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]