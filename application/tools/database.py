# -*- # -*- coding: utf-8 -*-

# Python
import getpass
import MySQLdb

# Django
from django.conf import settings

# Custom

class Database(object):

    def get_mysql_user(self):

        # Get .my.cnf to get mysql username
        me = getpass.getuser()
        if settings.HOSTNAME in settings.DEV_HOST:
            f = open('/home/{me}/.my.cnf'.format(me=me), 'r')    
        else:
            f = open('/root/.my.cnf', 'r')

        lines = f.readlines()

        for line in lines:
            line = line.replace('\n', '')
            if 'user' in line:
                user_line = line
        if user_line:
            user = user_line.split('=')[1]
            return user
        else:
            return None

    def get_mysql_password(self):

        # Get .my.cnf to get mysql password
        me = getpass.getuser()
        if settings.HOSTNAME in settings.DEV_HOST:
            f = open('/home/{me}/.my.cnf'.format(me=me), 'r')    
        else:
            f = open('/root/.my.cnf', 'r')

        # Read the file
        lines = f.readlines()

        # Search for password
        for line in lines:
            line = line.replace('\n', '')
            if 'password' in line:
                password_line = line

        if password_line:
            password = password_line.split('=')[1]
            return password
        else:
            return None
