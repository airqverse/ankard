FROM nginx:1.28.0

# NGINX_CONF is defined in docker-compose.yml to separate prod and dev.
ARG NGINX_CONF=default.prod.conf
COPY ${NGINX_CONF} /etc/nginx/conf.d/default.conf
