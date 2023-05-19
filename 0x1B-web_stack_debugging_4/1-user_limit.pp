# change OS user limit for open file descriptors
exec {'change OS config for holberton user':
  command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 4096/" /etc/security/limits.conf &&
sed -i "s/holberton soft nofile 4/holberton soft nofile 4096/" /etc/security/limits.conf',
  path    => ['/usr/bin', '/bin', 'usr/sbin']
}
