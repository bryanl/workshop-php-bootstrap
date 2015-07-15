# Docker and our application

Once we have our application running in Docker, we can move it to production. Starting resources by hand is a cumbersome and error-prone task. Docker provides us an automation tool, Docker Compose. It is configured with a docker-compose.yml file.

## Lab 5: Dockerizing our application

1. Create Docker Machine for our App
```sh
docker-machine create -d digitalocean \
  --digitalocean-size 2gb <identifier>-clickapp 
eval $(docker-machine env <identifer>-clickapp)
```

1. Configure Mysql container
```sh
docker run -d --name mysql -p 3306:3306 -e 'MYSQL_ROOT_PASSWORD=secure' -e 'ON_CREATE_DB=myapp' mysql
```