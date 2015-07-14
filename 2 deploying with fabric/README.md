# Deploying with Fabric

In this workshop, we will be working with a simple deployment. The deployment will consist of a web application backed by a database.

## Reviewing our application

Our application relies on three components:

1. Mysql is used to store our application's data. The data stored will be x and y coordinates of the mouse's click.
2. PHP application to store and load click coordinates.
3. Javascript application to collect and show click coordinates.

## Introducing Fabric

Fabric is a tool written in Python that be used to install apps and run commands on remote servers. Tasks are created to facilitate the actions.

```python
def host_type():
    run('uname -s')
```    

## Lab: 3 Deploying our Application

In this lab, we will create a new server, and deploy our application.

1. Create a new Droplet to serve as your application server.  
```sh
doit droplet create --droplet-name <identifer>-fab --region nyc3 --size 2gb --ssh-keys <ssh key id> --image ubuntu-14-04-x64
```

1. Bootstrap your server
```sh
fab -H root@<server ip> bootstrap
```

1. Configure your DB
```sh
fab -H root@<server ip> db_setup
```
