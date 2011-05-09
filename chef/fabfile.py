from fabric.api import env, local, run, sudo
env.user = 'ubuntu'
env.hosts = ['46.137.95.92']

env.key_filename = "/Users/phil/.ssh/phil-private.pem"
server_path = "/home/ubuntu/django_sites/biotech/company"
env.chef_executable = '/var/lib/gems/1.8/bin/chef-solo'
chef_solo_path = "/etc/chef/"
env.virtualenv = '/home/ubuntu/.virtualenvs/biotech'
#env.code_dir = '/home/docs/sites/readthedocs.org/checkouts/readthedocs.org'
#env.rundir = '/home/docs/sites/readthedocs.org/run'

def install_chef():
    sudo('apt-get update', pty=True)
    sudo('apt-get install -y git-core rubygems ruby ruby-dev subversion', pty=True)
    sudo('gem install chef --no-ri --no-rdoc', pty=True)
    sudo('mkdir -p %s'%chef_solo_path)
    sudo('chown ubuntu:ubuntu %s'%chef_solo_path)
    sudo('gem install haml') # installs sass
    sudo('apt-get install libopenssl-ruby')
    sudo('apt-get install nmap')


def sync_config():
    local('rsync -av  -e "ssh -v -v -v -i %s" . %s@%s:%s' % \
                                    (env.key_filename, env.user, env.hosts[0],
                                    chef_solo_path))


def update():
    sync_config()
    sudo('cd %s && %s' % (chef_solo_path, env.chef_executable), pty=True)

def reload():
    "Reload the server."
    env.user = "ubuntu"
    run("kill -HUP `cat %s/gunicorn.pid`" % env.rundir, pty=True)

def restart():
    "Restart (or just start) the server"
    sudo('restart biotech-gunicorn', pty=True)