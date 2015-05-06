FROM ubuntu
# os dependencies
RUN apt-get update && \
apt-get install -y \
	libpq-dev \
	nginx \
	python-dev \
	python-pip
# add code
ADD . /src 
RUN pip install -r src/AviPost/requirements/ci.txt

