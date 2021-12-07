FROM python:3.10.0b2-buster
EXPOSE 5000
VOLUME /usr/src/app
COPY . .
RUN pip install -r requirements.txt
CMD python main.py
