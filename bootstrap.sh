#!/usr/bin/env bash

apt-get update

# Python base packages
apt-get install -y  python python-pip

# Server and WSGI: apt-get install -y apache2 apache2-prefork-dev libapache2-mod-wsgi

# Database
echo 'mysql-server mysql-server/root_password password toor' | debconf-set-selections
echo 'mysql-server mysql-server/root_password_again password toor' | debconf-set-selections 
apt-get install -y mysql-server
apt-get install -y python-mysqldb

# Django framework
pip install Django==1.6.1

# Create a symbolic link to the project into the home dir
ln -s /vagrant/DjangoLibraryApp /home/vagrant

# Create the main MySQL database
echo "CREATE DATABASE DjangoLibraryApp" | mysql -u root -ptoor

# Create necessary Django database tables for INSTALLED_APPS
cd /vagrant/DjangoLibraryApp
echo -e "yes\nroot\nscoppino.giuseppe@gmail.com\ntoor\ntoor" | python manage.py syncdb
