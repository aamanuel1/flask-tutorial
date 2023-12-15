FROM python:3.9-slim
WORKDIR /usr/src/app
COPY . .
RUN pip install Flask
EXPOSE 5000
CMD ["flask", "--app", "flaskr", "init-db"]
