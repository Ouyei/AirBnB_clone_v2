#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the
# contents of the web_static folder of your AirBnB Clone
# repo, using the function do_pack.
from datetime import datetime
from fabric.api import local


def do_pack():
    """Generates a .tgz archive from the contents
    of the web_static folder of this repository.
    """

    d = datetime.now()
    now = d.strftime('%Y%m%d%H%M%S')

    local("mkdir -p versions")
    check = local('tar -cvzf {} web_static'.format(now))
    if check.failed:
        return None
    else:
        return now
