FROM python:alpine3.20
WORKDIR /app

COPY . .
RUN pip install -r requirements.txt
ENV PORT=8123

EXPOSE 8123
CMD [ "python3", "-m" , "flask", "--app", "server", "run", "--host=0.0.0.0"]
