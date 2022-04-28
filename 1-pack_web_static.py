#!/usr/bin/python3
# Fabric script that generates a .tgz archive from
# the contents of the web_static folder of your AirBnB Clone
# repo, using the function do_pack
"""Fabric file"""
from fabric.api import *
import datetime


def do_pack():
    """Do_pack function"""
    today = datetime.datetime.now()
    now = today.strftime('%Y%m%d%H%M%S')

    local('mkdir -p versions')
    check = local('tar -cvzf {} web_static'.format(now))
    if check.failed:
        return None
    else:
        return now
