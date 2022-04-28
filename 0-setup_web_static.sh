#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static
sudo apt-get -y update

# Install nginx
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
# Create folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create HMTL 
sudo touch /data/web_static/releases/test/index.html
echo "
<html>
 <head>
   <title>
   Holberton School
   </title>
 </head>
 
 <body>
   Holberton School
 </body>
 </html>" > sudo /data/web_static/releases/test/index.html

# Symbolic link
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current

# Create ownership
sudo chown -R ubuntu:ubuntu /data/

# Setup nginx
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ {alias /data/web_static/current/;}' /etc/nginx/sites-available/default

#Restart nginx
sudo service nginx restart
