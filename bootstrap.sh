#!/usr/bin/env bash

apt-get update

# Python base packages
apt-get install -y  python python-pip

# Server and WSGI: apt-get install -y apache2 apache2-prefork-dev libapache2-mod-wsgi

# Database
echo 'mysql-server-5.5 mysql-server/root_password password ' | sudo debconf-set-selections
apt-get install -y mysql-server-5.5
apt-get install -y python-mysqldb

# Django framework
pip install Django==1.6.1

ln -s /vagrant/DjangoLibraryApp /home/vagrant
