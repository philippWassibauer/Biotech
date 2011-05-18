
===============
Project Biotech
===============

Clone or copy this project to your computer.

----------
 Install on MacOsX
----------
 * Install XCode (you can find it on a MacOsX Installation CD in the Optional Install Folder, or download it at connect.apple.com)
 * Install Git and your Github Keys (http://help.github.com/key-setup-redirect/)
   I never use a passphrase, since it is quite annoying (personal opinion)
 * Install Setuptools
     http://pypi.python.org/pypi/setuptools choose the right version or use this:
     http://pypi.python.org/packages/2.6/s/setuptools/setuptools-0.6c11-py2.6.egg. if you have wget: (wget http://pypi.python.org/packages/2.6/s/setuptools/setuptools-0.6c11-py2.6.egg)
     otherwise download it to your computer
     run it as a shell script:
     sudo sh setuptools-0.6c9-py2.4.egg
 * sudo easy_install fabric (Used for deployment and automatisation of the Project)
 * git clone https://github.com/philippWassibauer/Biotech.git (Clone Project to directory)
 * cd /path/to/project/ (Go to project directory using the Terminal) - either company/ or cpm.biotech.at/
 * fab initialize (installs core dependencies)
 * fab install (installs application dependencies) - Take a coffee break. This takes a while
 * fab init_db (creates your database)
 * workon biotech (links all the packages installed previously to your terminal)
 * ./manage.py runserver (starts server)
 * now go to http://localhost:8000 and enjoy
