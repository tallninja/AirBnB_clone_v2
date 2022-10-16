#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder
"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """
    Funtion that compress a folder
    """
    try:
        local('mkdir -p versions')
        date = datetime.now()
        format = "%Y%m%d%H%M%S"
        path = 'versions/web_static_{}.tgz'.format(date.strftime(format))
        local('tar -cvzf {} web_static'.format(path))
        return path
    except Exception as error:
        return None
