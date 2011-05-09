app = node.run_state[:current_app]


directory "/home/ubuntu/.virtualenvs" do
    owner "ubuntu"
    group "ubuntu"
    mode 0775
end

virtualenv "/home/ubuntu/.virtualenvs/biotech" do
    owner "ubuntu"
    group "ubuntu"
    mode 0775
end

directory "/home/ubuntu/.virtualenvs/biotech/checkouts" do
    owner "ubuntu"
    group "ubuntu"
    mode 0775
end

git "/home/ubuntu/.virtualenvs/biotech/checkouts/biotech.at" do
    repository "git://github.com/philippWassibauer/Biotech.git"
    reference "HEAD"
    user "ubuntu"
    group "ubuntu"
    action :sync
end

script "Install Requirements" do
    interpreter "bash"
    user "ubuntu"
    group "ubuntu"
    code <<-EOH
     /home/ubuntu/.virtualenvs/biotech/bin/pip install -r /home/ubuntu/.virtualenvs/biotech/checkouts/biotech.at/company/requirements/project.txt
    EOH
end

# Gunicorn setup
cookbook_file "/etc/init/biotech-gunicorn.conf" do
    source "gunicorn.conf"
    owner "ubuntu"
    group "ubuntu"
    mode 0644
    #notifies :restart, resources(:service => "biotech-gunicorn")
end

service "biotech-gunicorn" do
    provider Chef::Provider::Service::Upstart
    enabled true
    running true
    supports :restart => true, :reload => true, :status => true
    action [:enable, :start]
end


cookbook_file "/home/ubuntu/.bash_profile" do
    source "bash_profile"
    owner "ubuntu"
    group "ubuntu"
    mode 0755
end


group "mysql" do
    gid 877
end


user "mysql" do
    comment "Mysql User"
    uid "1012"
    gid "mysql"
    password "$6$7jF6rAmF$GD.BjY.0KBkb.6SOCo3jEfyyDFyOk6tG70nXqB39LlKyku3hMQ.T/p7DKR2NxG/yD1bWer7LPnPyZd/NesSft/"
end

directory "/var/lib/mysql" do
    owner "mysql"
    group "mysql"
    mode 0775
end

include_recipe "mysql::server_ec2"
package "mysql-server" do
  action :install
end


mysql_database "create company_production database" do
  host "localhost"
  username "root"
  database "company_production"
  action :create_db
end