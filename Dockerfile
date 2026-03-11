FROM python:3.11

# Install nginx and supervisor
RUN apt-get update && apt-get install -y nginx supervisor && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY . /app
WORKDIR /app

# Create data directory for SQLite persistence
RUN mkdir -p /app/data

# Nginx config
COPY nginx.conf /etc/nginx/sites-available/default

# Supervisor config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Copy and set entrypoint (runs migrations at container start, not build time)
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]