FROM python:3.8-slim-buster
LABEL version="1.1"
LABEL description="This is the container for our backend"

WORKDIR /code/backend/src

# COPY package.json /code/backend/
# COPY package-lock.json /code/backend/
# COPY setup.sh /code/backend
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 4000

# CMD ["sleep", "infinity"]
# CMD ["python3", "/code/backend/main.py"]

CMD ["flask",  "run",  "--host=0.0.0.0",  "--port=4000"]