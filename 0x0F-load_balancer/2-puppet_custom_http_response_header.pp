#!/usr/bin/env bash
class nginx {
  package { 'nginx':
    ensure => installed,
  }

  file { '/var/www/html/index.html':
    content => "Holberton School\n",
    ensure => file,
  }

  file { '/var/www/html/404.html':
    content => "Ceci n'est pas une page\n",
    ensure => file,
  }

  file { '/etc/nginx/sites-available/default':
    content => "server {
                  listen 80 default_server;
                  listen [::]:80 default_server;
                  add_header X-Served-By $hostname;
                  root /var/www/html;
                  index index.html index.htm;

                  location /redirect_me {
                    return 301 http://cuberule.com/;
                  }

                  error_page 404 /404.html;
                  location /404 {
                    root /var/www/html;
                    internal;
                  }
                }",
    ensure => file,
    notify => Service['nginx'],
  }

  service { 'nginx':
    ensure => running,
    enable => true,
    require => File['/etc/nginx/sites-available/default'],
  }
}

include nginx
