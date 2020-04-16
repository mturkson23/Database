# Dockerfile

FROM python:3.7-buster

# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# copy source and install dependencies
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/MicroBiome
COPY MicroBiome/requirements/dev.txt start-server.sh /opt/app/
COPY .pip_cache /opt/app/pip_cache/
COPY MicroBiome /opt/app/MicroBiome/
COPY Database /opt/app/Database/
COPY db.sqlite3 /opt/app/
WORKDIR /opt/app

RUN pip install -r MicroBiome/requirements/dev.txt --cache-dir /opt/app/pip_cache
RUN chown -R www-data:www-data /opt/app

# start server
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]

