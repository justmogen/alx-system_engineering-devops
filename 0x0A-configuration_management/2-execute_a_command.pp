# This manifest kills a process named killmenow only if it is running 
exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
  onlyif  => '/usr/bin/pgrep killmenow',
  path    => ['/usr/bin', '/bin'],
}
