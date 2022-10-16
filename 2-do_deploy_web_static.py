#!/usr/bin/python3
from fabric.api import *
from os.path import exists
from datetime import datetime
import os.path

env.hosts = ['54.210.85.213', '54.91.141.251']
env.user = 'ubuntu'
env.key = "~/.ssh/school"


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


def do_deploy(archive_path):
    """Deployment process (distributing an archive to the web server"""

    if not exists(archive_path):
        return False

    try:
        file_formatted = archive_path.split(".")[0].split("/")[1]
        folder = "/data/web_static/releases/"
        final_path = "{}{}".format(folder, file_formatted)

        put(archive_path, "/tmp/{}.tgz".format(file_formatted))
        run("mkdir -p {}/".format(final_path))
        run("tar -xzf /tmp/{}.tgz -C {}/".format(file_formatted, final_path))
        run("rm /tmp/{}.tgz".format(file_formatted))
        run("mv {}/web_static/* {}".format(final_path, final_path))
        run("rm -rf {}/web_static".format(final_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(final_path))
        return True

    except Exception:
        return False
