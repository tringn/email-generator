FROM python:3.11.8-slim

# Non-interactive docker build
ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && apt upgrade -y

WORKDIR /src

ENV PYTHONPATH=/src

COPY requirements.txt /src/

RUN pip install -r requirements.txt

COPY . /src/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
