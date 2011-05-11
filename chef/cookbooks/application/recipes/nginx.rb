package "nginx" do
    :upgrade
end

service "nginx" do
  enabled true
  running true
  supports :status => true, :restart => true, :reload => true
  action [:start, :enable]
end

cookbook_file "/etc/nginx/sites-enabled/biotech" do
  source "nginx/biotech"
  mode 0640
  owner "ubuntu"
  group "ubuntu"
  notifies :restart, resources(:service => "nginx")
end

cookbook_file "/etc/nginx/nginx.conf" do
  source "nginx/nginx.conf"
  mode 0640
  owner "ubuntu"
  group "ubuntu"
  notifies :restart, resources(:service => "nginx")

end
