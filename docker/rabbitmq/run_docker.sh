#!/bin/bash

docker run --rm -it \
    -p 127.0.0.1:5672:5672 \
    -p 127.0.0.1:25672:25672 \
    --hostname my-rabbit-node \
    --name my-rabbit rabbitmq:3.7-alpine
