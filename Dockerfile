FROM python:3.8.3-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN export PATH="$PATH:~/.yarn/bin"

RUN mkdir /code
WORKDIR /code

ADD ./front/conf/requirements.txt /code/
RUN apk add --update \
    gcc \
    py-pip \
    build-base \
    git \
    wget \
    libxslt-dev \
    xmlsec-dev \
    mariadb-dev \
    libressl-dev \
    unixodbc \
    unixodbc-dev \
    curl

RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

# RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD ./ /code/

ARG DJANGO_APP
ENV DJANGO_APP=${DJANGO_APP}
EXPOSE 8090
CMD sh -c "gunicorn --bind 0.0.0.0:8090 ${DJANGO_APP}.wsgi:application"
