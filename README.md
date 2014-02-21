DjangoLibraryApp
================

A web application which manages a virtual database of library books and clients, built using the Django framework.

Usage
================

- Install Vagrant

- cd into the project directory, and run 'vagrant up' to build and start the VM.

- Run 'vagrant ssh' to SSH into the VM

- cd into the project directory (it should be a sub-folder of the initial working directory)

- Run 'python manage.py runserver 0.0.0.0:8000' to bring up the test server

- Point your web browser to localhost:8080 to use the web app. Go to localhost:8080/admin to 
  use the administrative control panel. Username is root, Password is toor.

- When you are done with work, press Ctrl+C to kill the server, type 'exit' to exit
  the SSH session, and type 'vagrant halt' in the project directory to shutdown the VM

- Next time, you want to use the VM, just type 'vagrant up'; this time the VM will be already 
  built. Then enter the project directory and run the server as before
