# install nginx and add custom header
package {'nginx':
        ensure => installed
}

file_line {'custom_header':
  path  => '/etc/nginx/sites-available/default',
  after => 'server_name _;',
  line  => '#n\n\tadd_header $hostame;'
}

service {'nginx':
  ensure => running
}
