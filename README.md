DjangoLibraryApp
================

A web application which manages a virtual database of library books and clients, built using the Django framework.

Usage
================

- Clone this repository into a folder of your choice

- Install Vagrant

- Use the 'cd' command to navigate into the project directory from the CLI, 
  and run 'vagrant up' to build and start the VM.

- Run 'vagrant ssh' to SSH into the VM

- cd into the project directory (it should be a sub-folder of the initial working directory)

- Run 'python manage.py shell' to bring up a Python shell

- Type 'execfile('ImportScript.py')' in the python shell to import test books into the database.

- Type 'execfile('SetupScript.py')' in the python shell to creates test shelves, libraries, and assign
  random books to shelves.

- Run 'python manage.py runserver 0.0.0.0:8000' to bring up the test server

- Point your web browser to localhost:8080 to use the web app. Go to localhost:8080/admin to 
  use the administrative control panel. Username for both is root, Password for both is toor.

- When you are done with work, press Ctrl+C to kill the server, type 'exit' to exit
  the SSH session, and type 'vagrant halt' in the project directory to shutdown the VM

- Next time, you want to use the VM, just type 'vagrant up'; this time the VM will be already 
  built. Then enter the project directory and run the server as before.

- If there are any questions, feel free to email me at scoppino.giuseppe@gmail.com or
  gscoppin@spsu.edu.
