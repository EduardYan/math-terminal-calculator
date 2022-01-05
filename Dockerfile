FROM alpine:3.15

RUN apk add python3 \
    && apk add py3-pip \
    && pip install --upgrade pip

# workdir
WORKDIR /calculator

COPY . .

# dependencies
RUN pip install -r requirements.txt

CMD ["python3", "main.py"]