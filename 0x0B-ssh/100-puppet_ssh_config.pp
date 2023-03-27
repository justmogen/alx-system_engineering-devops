#!/usr/bin/env bash
file {'/home/justmogen/alx-system_engineering-devops/0x0B-ssh/2-ssh_config':
	ensure => file,
	owner => 'justmogen',
	group => 'justmogen',
	mode => '744',
	content => '
Host just
	IdentityFile ~/.ssh/school
	PasswordAuthentication no',

}
