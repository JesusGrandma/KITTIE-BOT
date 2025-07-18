FROM python:3.11-slim-bookworm

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libffi-dev \
    libnacl-dev \
    python3-dev \
    gcc \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python3.11 -m pip install -U git+https://github.com/Rapptz/discord.py

COPY . .

ENV YTDLP_CONFIG_PATH=/app/config/yt-dlp.conf
RUN mkdir -p /app/config && \
    echo "ffmpeg-location /usr/bin/ffmpeg\nno-check-certificate" > /app/config/yt-dlp.conf

CMD ["python", "bot.py"]
