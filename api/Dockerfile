FROM python:3.10
WORKDIR /app
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
COPY requirements.txt /app
RUN pip install -r /app/requirements.txt --no-cache-dir

COPY . /app/
CMD chmod +x /app/entrypoint.sh && /app/entrypoint.sh