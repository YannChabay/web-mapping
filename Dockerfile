FROM python:3.12-slim

# rootless user
RUN useradd -m pyscraper

# updates & requirements installation
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY pyscript.py /app/pyscript.py

WORKDIR /app

# connects to the user
USER pyscraper

ENTRYPOINT ["python", "/app/pyscript.py"]
