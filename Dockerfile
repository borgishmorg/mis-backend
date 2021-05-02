FROM python:3.9

COPY . /api
WORKDIR /api
RUN pip install -r requirements.txt
CMD [ "python", "run.py" ]
