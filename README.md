# docker-images

## python3.6-supervisor
```bash
docker build -f DockerfileBase -t cnas-base:latest .
docker build -t cnas-app:latest .

docker run -d --name rabbitmq -p 15672:15672 -p 5672:5672 rabbitmq:3.7.15-management
docker run --name worker -e RABBIT_HOST=localhost -e RABBIT_PORT=5672 cnas-app:latest worker
docker run -d --name flask -e WEB_PORT=8000 -p 8000:8000 cnas-app:latest flask
```

or

```bash
docker-compose up
```

```bash
docker-compose stop
```

```bash
docker-compose rm
```

```bash
docker-compose logs
```
