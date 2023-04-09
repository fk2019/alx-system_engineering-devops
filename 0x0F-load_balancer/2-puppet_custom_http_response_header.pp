# install nginx and add custom header
package {'nginx':
        ensure => installed
}

file_line {'custom_header':
  path  => '/etc/nginx/sites-available/default',
  after => 'server_name _;',
  line  => "\n\tadd_header \$HOSTNAME;"
}

service {'nginx':
  ensure => running
}
