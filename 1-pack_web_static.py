#!/usr/bin/python3
"""script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo"""

from fabric.api import local
from datetime import datetime

def do_pack():
    """packages all contents from web_static into .tgz archive"""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    output = local(f"tar -czvf versions/web_static_{now}.tgz web_static")
    if output.failed:
        return None
    return output
