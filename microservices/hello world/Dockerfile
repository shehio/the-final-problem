FROM alpine:latest
RUN apk add --no-cache python3 py3-pip
RUN pip3 install flask
COPY app.py /app/
EXPOSE 9000
CMD ["python3", "/app/app.py"]