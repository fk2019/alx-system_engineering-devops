# execute pkill command on killmenow process
exec {'kill killmenow':
  command => '/usr/bin/pkill killmenow',
  path    => ['/usr/bin/pkill', 'usr/sbin/pkill']
}
