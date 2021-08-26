#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy:"""
from fabric.api import env
from fabric.api import run
from fabric.api import put
from fabric.api import local
from datetime import datetime
from os import path as p


env.hosts = ['34.139.131.104', '34.139.28.201']


def do_pack():
        """function do_pack must return the archive path
        if the archive has been correctly generated.
        Otherwise, it should return None"""
        dt = datetime.now()
        y = str(dt.year)
        M = str(dt.month)
        d = str(dt.day)
        h = str(dt.hour)
        m = str(dt.minute)
        s = str(dt.second)
        time = y + M + d + h + m + s
        try:
                local("mkdir versions")
                local("tar -cvzf versions/web_static_{}.tgz web_static"
                      .format(time))
                return "versions/web_static_{:s}.tgz".format(time)
        except:
                return None


def do_deploy(archive_path):
        """Returns True if all operations have been done
        correctly, otherwise returns False"""
        if not p.exists(archive_path):
                return False
        try:
                put(archive_path, '/tmp')
                path = archive_path.split('/')
                file = path[1].split('.')
                run("mkdir -p /data/web_static/releases/{}"
                    .format(file[0]))
                run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
                    .format(path[1], file[0]))
                run("rm /tmp/{}".format(path[1]))
                run("mv /data/web_static/releases/{}/web_static/*\
                /data/web_static/releases/{}".format(file[0], file[0]))
                run("rm -rf /data/web_static/releases/{}/web_static"
                    .format(file[0]))
                run("rm -rf /data/web_static/current")
                run("ln -s /data/web_static/releases/{}\
                /data/web_static/current".format(file[0]))
                return True
        except:
                False
