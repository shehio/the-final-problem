FROM python:3.12-alpine
RUN pip install --no-cache-dir flask
COPY app.py /app/
EXPOSE 9000
CMD ["python3", "/app/app.py"]
