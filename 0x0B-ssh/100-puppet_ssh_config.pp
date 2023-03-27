#!/usr/bin/env bash
file_line { 'Turn off passwd auth':
  path  => '/home/justmogen/alx-system_engineering-devops/0x0B-ssh/2-ssh_config',
  line  => 'PasswordAuthentication no',
  match => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
  path  => '/home/justmogen/alx-system_engineering-devops/0x0B-ssh/2-ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^#?IdentityFile',
}
