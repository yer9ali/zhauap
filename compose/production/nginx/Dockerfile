FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf \
&& mkdir -p /app/staticfiles \
&& mkdir -p /app/daiyn_zhauaptar/mediafiles \
&& mkdir -p /etc/nginx/ssl

RUN chown -R www-data:www-data /app/daiyn_zhauaptar/mediafiles \
&& chmod -R 777 /app/daiyn_zhauaptar/mediafiles

RUN chmod -R 777 /app/staticfiles

#ADD ./ssl /etc/nginx/ssl/

CMD ["nginx", "-g", "daemon off;"]
