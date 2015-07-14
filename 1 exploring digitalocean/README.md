# Exploring DigitalOcean

DigitalOcean is an Infrastructure as a Service provider. What that means is we provide virtual compute resources which you can run your applications on. DigitalOcean provides multiple operating systems and applications you can build on. We call these compute resources Droplets. 

## Booting a DigitalOcean Droplet

As a warm up exercise, we can practice booting up Droplets using the Cloud GUI.

![](images/create_droplet.png)

DigitalOcean provides a myriad of options for configuring your Droplet.

You can select size...

![](images/size.png)

And Region...

![](images/region.png)

And the type of Image...

![](images/image-dist.png)

Images can also be wholly configured applications...

![](images/image-app.png)

You can configure settings...

![](images/settings.png)

And provide a SSH key...

![](images/ssh-keys.png)

## Lab 1: Creating a DigitalOcean Droplet

In our first lab, we'll create a Droplet that will serve as our home base. This will be easier as it won't require any local configuration on your computer.


## DigitalOcean's API

This isn’t the only way to create Droplets. We can also use the DigitalOcean API to create Droplets. To use our API, you’ll have to generate an API token.

![](images/token.png)

The DigitalOcean API has a documentation site at [https://developers.digitalocean.com/documentation/v2/](https://developers.digitalocean.com/documentation/v2/)

![](images/api-home.png)

## Lab 2: Using the DigitalOcean API

In this lab, we will use the DigitalOcean API to create a Droplet from the command line.