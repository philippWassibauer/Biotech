from fabric.api import env, local, run, sudo
env.user = 'ubuntu'
env.hosts = ['46.137.95.92']

env.key_filename = "/Users/phil/.ssh/phil-private.pem"
server_path = "/home/ubuntu/.virtualenvs/biotech/checkouts/biotech.at/company"
env.chef_executable = '/var/lib/gems/1.8/bin/chef-solo'


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


def deploy():
    local("git commit -a -m 'quick update'")
    local("git push origin master")
    with cd(server_path):
        run('git pull origin master')
        run("workon biotech; python manage.py collectstatic --noinput;")
        