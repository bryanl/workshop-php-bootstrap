# Starting with Docker

From the Docker website, we can find this description:

> Docker allows you to package an application with all of its dpendencies into a standardized uint for software development.

What this means is Docker allows you to create an individual container that contains all the necessary components your application needs to run: from the code, to the filesystem, and libraries. The app will be mostly segregated from the existing operating system, but all containers will share the same kernel. It differs from a virtual machine because it doesn't boot up another operating system. It's a process like the others than run on your server.

## Lab 4: Starting with Docker

1. Boot workshop console

1. Create an a docker-machine instance.
```sh
docker-machine create -d digitaocan dev-<identifier>
eval $(docker-machine env dev-<identifier>)
docker ps
env | grep DOCKER
```

1. Create your first Docker instance
```sh
docker run -i -t --rm ubuntu /bin/bash
```
1. Start a Redis container
```sh
docker pull redis
docker run -d --name redis redis
docker ps
```

1. Connect to your Redis instance using Redis CLI
```sh
docker run -i -t --rm --link redis:redis redis redis-cli -h redis
```

