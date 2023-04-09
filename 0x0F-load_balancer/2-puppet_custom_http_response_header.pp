# install nginx and create redirects
package {'nginx':
        ensure => installed
}

exec {'add_header':
  provider => shell,
  command  => 'sudo sed -i "/server_name _;/a \#t\tadd_header X-Served-By \$HOSTNAME;" /etc/nginx/sites-available/default;
  service nginx start'
}
