# install nginx and add custom header
package {'nginx':
        ensure => installed
}

file_line {'redirections':
  path  => '/etc/nginx/sites-available/default',
  after => 'server_name _;',
  line  => "#n\n\tadd_header \$HOSTNAME;"
}

service {'nginx':
  ensure => running
}
