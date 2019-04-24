# ./container/Dockerfile
FROM ubuntu:xenial
ADD ./bar_kit/nginx /code
WORKDIR /code
RUN chmod +x start-certbot.sh
#CMD [ "/bin/bash" ]
ENTRYPOINT [ "./start-certbot.sh" ]