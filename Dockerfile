FROM python:3.11

# Install nginx and supervisor
RUN apt-get update && apt-get install -y nginx supervisor

# Copy and install Python deps
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

# Nginx config
COPY nginx.conf /etc/nginx/sites-available/default

# Supervisor config (manages both processes)
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 80

CMD ["/usr/bin/supervisord"]