FROM python:3.12

WORKDIR /app

COPY . . 

RUN pip install flask flask-cors
RUN apt update && apt install -y bash

EXPOSE 5000

CMD ["python", "app.py"]
