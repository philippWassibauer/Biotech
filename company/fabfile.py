from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm
import settings as settings
import os
env.user = 'ubuntu'
env.hosts = ['46.137.95.92']

server_path = "/home/ubuntu/.virtualenvs/biotech/checkouts/biotech.at/company"
env.chef_executable = '/var/lib/gems/1.8/bin/chef-solo'
env.shell = "/bin/bash -li -c"
env.key_filename = "biotech.pem"
server_path = "/home/ubuntu/.virtualenvs/biotech/checkouts/biotech.at/biotech/"
env.chef_executable = '/usr/bin/chef-solo'

def initalize():
    # install dependencies
    (sysname, nodename, release, version, machine) = os.uname()
    if sysname == "Darwin":
        local('pip install -U pip')
        local('pip install virtualenv')
        local('pip install virtualenvwrapper')
        local('echo export WORKON_HOME=~/.virtualenvs >> ~/.bash_profile')
        local('echo mkdir -p \$WORKON_HOME >> ~/.bash_profile')
        local('echo source /usr/local/bin/virtualenvwrapper.sh >> ~/.bash_profile')
        local('mkvirtualenv --no-site-packages biotech')
    else:
        run('apt-get install libxml2-dev')
        run('apt-get install libxslt-dev')
        run('apt-get install python-dev')
        run('apt-get install build-essentials')
        run('apt-get intall python-pip')
        run('pip install -U pip')
        run('apt-get install git-core mercurial subversion')
        run('pip install setuptools')
        run('pip install virtualenv')
        run('pip install virtualenvwrapper')
        run('apt-get install nmap')
        run('echo export WORKON_HOME=~/.virtualenvs >> ~/.profile')
        run('echo mkdir -p \$WORKON_HOME >> ~/.profile')
        run('echo source /usr/local/bin/virtualenvwrapper.sh >> ~/.profile')
        run('mkvirtualenv --no-site-packages biotech')


def install():
    local("pip install -r requirements/projects.txt")

def init_db():
    local("./manage.py syncdb --all")
    local("./manage.py migrate --fake")

def dump_cms_data():
    local('./manage.py dumpdata cms text picture link file snippet googlemap mptt menus publisher --indent 4 > fixtures/cms.json')

def load_cms_data():
    local("./manage.py loaddata fixtures/cms.json")

def makemessages():
    makedbmessages() #this will pull fields out of db into python object, where they are picked up by the next call
    local('./manage.py makemessages -a -e ".html, .txt"')

def restart():
    "Restart (or just start) the server"
    sudo('restart biotech-gunicorn', pty=True)

def update_deploy():
    local("git commit -a -m 'quick update'")
    local("git push origin master")
    deploy()
    
def deploy():

    with cd(server_path):
        run('git pull origin master')
        run("workon biotech; python manage.py collectstatic --noinput;")
        