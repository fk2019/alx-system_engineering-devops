# fix bad wordpress php extension
exec { 'fix wordpress':
          command => '/bin/sed -i s/phpp/php/g /var/www/html/wp-settings.php',
          path    => ['/bin/sed']
}