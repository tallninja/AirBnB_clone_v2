#!/usr/bin/python3
"""a script to pack static content into a tarball"""

from fabric.api import *
from fabric.operations import put
from datetime import datetime
import os


env.hosts = ['3.239.117.62', '3.231.210.238']
env.user = 'ubuntu'
env.key = "~/.ssh/school"


def do_pack():
    """packages all contents from web_static into .tgz archive"""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local('mkdir -p versions')
    res = local('tar -cvf versions/web_static_{}.tgz web_static'
                .format(now))
    if res.failed:
        return None
    else:
        return


def do_deploy(archive_path):
    """deploys a static archive to web servers
    """
    if not os.path.isfile(archive_path):
        print('archive file does not exist...')
        return False
    try:
        archive = archive_path.split('/')[1]
        no_ext_archive = archive.split('.')[0]
    except Exception as e:
        print('failed to get archive name from split...')
        return False
    uploaded = put(archive_path, '/tmp/')
    if uploaded.failed:
        return False
    res = run('mkdir -p /data/web_static/releases/{}/'.format(no_ext_archive))
    if res.failed:
        print('failed to create archive directory for relase...')
        return False
    res = run('tar -C /data/web_static/releases/{} -xzf /tmp/{}'.format(
               no_ext_archive, archive))
    if res.failed:
        print('failed to untar archive...')
        return False
    res = run('rm /tmp/{}'.format(archive))
    if res.failed:
        print('failed to remove archive...')
        return False
    res = run('mv /data/web_static/releases/{}/web_static/* \
               /data/web_static/releases/{}'
              .format(no_ext_archive, no_ext_archive))
    if res.failed:
        print('failed to move extraction to proper directory...')
        return False
    res = run('rm -rf /data/web_static/releases/{}/web_static'
              .format(no_ext_archive))
    if res.failed:
        print('failed to remove first copy of extraction after move...')
        return False
    # clean up old release and remove it
    res = run('rm -rf /data/web_static/current')
    if res.failed:
        print('failed to clean up old release...')
        return False
    res = run('ln -sfn /data/web_static/releases/{} /data/web_static/current'
              .format(no_ext_archive))
    if res.failed:
        print('failed to create link to new release...')
        return False

    print('\nNew Version Successfuly Deployed!\n')

    return True
