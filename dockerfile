FROM python:3.11-slim-bookworm

ENV DEBIAN_FRONTEND=noninteractive PIP_NO_CACHE_DIR=1

RUN apt-get update \
 && apt-get -y upgrade \
 && apt-get install -y --no-install-recommends build-essential git curl \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --upgrade pip \
 && pip install -r requirements.txt

COPY . .

RUN useradd -m appuser
USER appuser

ENV PORT=7860
EXPOSE 7860

CMD ["streamlit", "run", "main.py", "--server.port", "7860", "--server.address", "0.0.0.0", "--server.headless", "true"]
