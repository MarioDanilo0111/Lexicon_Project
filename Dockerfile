FROM python:3.11-slim-bookworm

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Only install what you actually need (adjust if you compile libs)
RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential git curl \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install deps first for better caching
COPY requirements.txt .
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

# Copy app
COPY . .

# Non-root
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Streamlit must bind 0.0.0.0 and respect $PORT (HF/Render/Fly set this)
ENV PORT=7860
EXPOSE 7860

CMD streamlit run main.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true

