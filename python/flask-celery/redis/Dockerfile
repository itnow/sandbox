FROM redis:4-alpine

COPY ./conf/redis.conf /home/redis/redis.conf

WORKDIR /data

EXPOSE 6379

CMD ["redis-server", "/home/redis/redis.conf"]

