#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

MY_ID=28236
HOST_NAME=$(hostname)
STATIC="/data/web_static/"
CONFIG_FILE="/etc/nginx/sites-available/default"

# install nginx
sudo apt -y update
sudo apt -y install nginx

# check if hostname is configured properly
if [[ $(hostname) =~ ^$MY_ID-web-[0-9]+ ]]; then
    echo 'hostname properly configured'
else
    (>&2 echo 'hostname not configured properly...')
    (>&2 echo "please set hostname to pattern: $MY_ID-web-<server_id>...")
    (>&2 echo "Example: sudo hostnamectl set-hostname $MY_ID-web-<insert_server_id_here>")
fi

sudo mkdir -p $STATIC/releases/
sudo mkdir -p $STATIC/shared/
sudo mkdir -p $STATIC/releases/test/
echo "Hello World!" | sudo tee $STATIC/releases/test/index.html
sudo ln -sfn $STATIC/releases/test/ $STATIC/current
sudo chown -fR ubuntu:ubuntu /data/

# update index.html file
echo "Hello World!" > index.html
sudo mv index.html /var/www/html
echo "Ceci n'est pas une page" > 404.html
sudo mv 404.html /var/www/html

printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    root   $STATIC/current;
    index  index.html index.htm;
    add_header X-Served-By $HOST_NAME;

    location / {
        alias $STATIC/current/;
    }

    location /redirect_me {
        return 301 https://github.com/tallninja;
    }

    location /hbnb_static {
        alias $STATIC/current/;
    }

    error_page 404 /404.html;

    location /404 {
      root /usr/share/nginx/html;
      internal;
    }
}" > default

sudo mv default $CONFIG_FILE

sudo service nginx restart
