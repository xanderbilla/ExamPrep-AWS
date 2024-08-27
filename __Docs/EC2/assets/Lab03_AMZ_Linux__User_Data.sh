#!/bin/bash

#script to launch a web server on an EC2 instance

#install apache
sudo yum update -y
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd

#create a simple web page
echo "<html><h1>Hello World</h1></html>" > /var/www/html/index.html

# launch the web server
sudo systemctl restart httpd
