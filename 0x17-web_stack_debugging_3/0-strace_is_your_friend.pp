# Fix the typo in /var/www/html/wp-settings

file { '/var/www/html/wp-settings.php':
ensure => file,
source => '/var/www/html/wp-settings.php',
content => file('/var/www/html/wp-settings.php').content.gsub('class-wp-locale.phpp', 'class-wp-locale.php'),
owner => 'www-data',
group => 'www-data',
mode => '0644',
notify => Service['apache2'],
}

service { 'apache2':
ensure => running,
enable => true,
require => File['/var/www/html/wp-settings.php'],
}
