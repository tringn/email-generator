FROM python:3.11.8-slim

RUN mkdir /client

COPY requirements.txt /client

WORKDIR /client

ENV PYTHONPATH=/client

RUN pip install -r requirements.txt

COPY . /client

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
