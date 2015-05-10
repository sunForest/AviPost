FROM python:2.7

# os dependencies
RUN apt-get update && \
apt-get install -y \
	libpq-dev \
    libgeos-dev \
	nginx
COPY deployment/avipost.conf /etc/nginx/sites-enabled/
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD . /usr/src/app/
RUN pip install -r requirements/prod.txt
RUN cd avipost/ && DJANGO_SETTINGS_MODULE=avipost.settings.ci gunicorn avipost.wsgi:application
RUN service nginx start

# CMD ['nginx', '-g', 'daemon off;']
