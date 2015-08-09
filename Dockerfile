FROM python:2.7

# os dependencies
RUN apt-get update && \
apt-get install -y \
	libpq-dev \
    python-dev \ 
    libpython-dev \
    libevent-dev \
    libgeos-dev \
	nginx \
    supervisor
COPY deployment/avipost.conf /etc/nginx/sites-enabled/
COPY deployment/supervisord.conf /etc/supervisord.conf
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD . /usr/src/app/
RUN pip install -r requirements/prod.txt

# restart nginx to load the config
RUN service nginx stop

CMD supervisord -c /etc/supervisord.conf -n

