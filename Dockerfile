FROM python:3.8

RUN apt update
RUN apt install python3

WORKDIR C:/Users/iris/Desktop/8semestre8/devops/tp2docker

COPY app.py ./

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python3", "./app.py" ]