sudo docker build -t redis-img ./redis
sudo docker run --rm -it \
    -p 127.0.0.1:6379:6379 \
    --mount type=bind,src="$(pwd)"/redis/data,dst=/data \
    --name redis-cont redis-img
