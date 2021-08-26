#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB Clone repo,
using the function do_pack"""
from fabric.api import local
from datetime import datetime


def do_pack():
        """The function do_pack must return the archive
        path if the archive has been correctly generated.
        Otherwise, it should return None
        """
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
                local("tar -cvzf versions/web_static_{}.tgz web_static".format(time))
                return "versions/web_static_{:s}.tgz".format(time)
        except:
                return None
