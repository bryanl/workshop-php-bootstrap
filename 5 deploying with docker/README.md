# Deploying with Docker

Once we have our application running in Docker, we can move it to production. Starting resources by hand is a cumbersome and error-prone task. Docker provides us an automation tool, Docker Compose. It is configured with a docker-compose.yml file.

In our last lab, we hand build our Docker setup. How do automate this?

# Lab 6: Deploying with Docker

1. Create new Docker Machine for our App
```sh
docker-machine create -d digitalocean \
  --digitalocean-size 2gb <identifier>-clickapp2 
eval $(docker-machine env <identifer>-clickapp2)
```

1. Use Docker Compose to build app
```sh
cd ~/workshop-php-bootstrap
docker-compose up -d
mysql -uadmin  -h $(docker-machine ip <identifier>-clickapp) -p  myapp < db/myapp.sql
```

1.  Review your website. Location is at `docker-machine ip <identifier>-clickapp`