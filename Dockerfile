FROM python:2.7

# os dependencies
RUN apt-get update && \
apt-get install -y \
	libpq-dev \
	nginx

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD . /usr/src/app
RUN pip install -r requirements/prod.txt

# TODO copy nginx configuration

CMD ['nginx', '-g', 'daemon off;']
