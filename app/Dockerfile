FROM python:3.6-slim
COPY ./beer_app.py /deploy/
COPY ./requirements.txt /deploy/
COPY ./app/gmm.pkl /deploy/
WORKDIR /deploy/
RUN pip install -r requirements.txt
EXPOSE 333
ENTRYPOINT ["python", "beer_app.py"]
