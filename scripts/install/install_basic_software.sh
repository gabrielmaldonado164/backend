#!/bin/bash

echo -n "Ingrese la clave: "
read -s PASSWORD
echo

touch /var/log/install.log

echo "[ INFO ]: Disable firewalld ; NetworkManager"
systemctl disable firewalld NetworkManager >> /var/log/install.log 2>&1
echo "[ INFO ]: Stop firewalld ; NetworkManager"
systemctl stop firewalld NetworkManager >> /var/log/install.log 2>&1

echo "[ INFO ]: Disable selinux"
echo -e "# This file controls the state of SELinux on the system.
# SELINUX= can take one of these three values:
#     enforcing - SELinux security policy is enforced.
#     permissive - SELinux prints warnings instead of enforcing.
#     disabled - No SELinux policy is loaded.
SELINUX=disabled
# SELINUXTYPE= can take one of three values:
#     targeted - Targeted processes are protected,
#     minimum - Modification of targeted policy. Only selected processes are protected. 
#     mls - Multi Level Security protection.
SELINUXTYPE=targeted" > /etc/selinux/config

echo -e "[ INFO ]: Install mlocate wget net-tools git vim python3 python3-devel gcc yum-utils epel-release."
yum install -y mlocate wget net-tools git vim python3 python3-devel gcc yum-utils epel-release >> /var/log/install.log 2>&1

echo -e "[ INFO ]: Configure bashrc"
echo -e "# .bashrc

# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
alias vi='vim'

export HISTFILESIZE=
export HISTSIZE=
export HISTTIMEFORMAT='[%F %T] '

# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi
" > /root/.bashrc

echo -e "[ INFO ]: Install mysql server."
yum install -y mariadb-server mariadb-devel >> /var/log/install.log 2>&1
echo -e "[ INFO ]: Starting and enabling mysql server."
systemctl enable mariadb >> /var/log/install.log 2>&1
systemctl start mariadb >> /var/log/install.log 2>&1

echo -e "[ INFO ] Configure mariadb server..."
mysql -e "UPDATE mysql.user SET Password = PASSWORD('$PASSWORD') WHERE User = 'root'"
mysql -e "DROP USER ''@'localhost'"
mysql -e "DROP USER ''@'$(hostname)'"
mysql -e "DROP DATABASE test"
mysql -e "FLUSH PRIVILEGES"

echo -e "[mysql]
user=root
password=$PASSWORD
" > /root/.my.cnf

echo  -e "[ INFO ] Configuring backend."
mysql -e "CREATE DATABASE backend"

echo -e "[ INFO ] Installing python modules."
pip3 install -r /opt/backend/application/requirements.txt

# Configuring APP
python3 /opt/backend/application/manage.py makemigrations
python3 /opt/backend/application/manage.py makemigrations schemas

python3 /opt/backend/application/manage.py migrate


