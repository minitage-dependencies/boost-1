#!/usr/bin/env python

# Copyright (C) 2009, Mathieu PASQUET <kiorky@cryptelium.net>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

__docformat__ = 'restructuredtext en'

import re
import platform
import os
import sys


from  subprocess import Popen, PIPE
from minitage.core.common import which



def get_install_name_tool():
    if sys.platform.lower() == 'darwin':
        return which('install_name_tool')

def get_otool():
    if sys.platform.lower() == 'darwin':
        return which('otool')


def get_rpath(lib):
    intool = get_otool()
    output = Popen([intool, '-L', lib], stdout=PIPE, stderr=PIPE)
    output.wait()
    content = output.stdout.read()
    rlibs = []
    if len(content.splitlines())>2:
        rlibs = [b[0] for b in [a.split() for a in content.splitlines()[1:]]]
    return rlibs

def relink(options, buildout):
    libdir = os.path.join(
        buildout['part']['location'], 'lib'
    )
    if sys.platform.lower() == 'darwin':
        libs = [a for a in os.listdir(libdir) if 'dylib' in a]
        for i in libs:
            ip = os.path.join(libdir, i)
            os.system('install_name_tool -id %s %s' % (ip, ip))
            rlibs = get_rpath(ip)
            for lib in rlibs:
                jp = os.path.join(libdir, lib)
                if lib in libs:
                    os.system('install_name_tool -change %s %s %s' % (lib, jp, ip))

def hook(options=None,buildout=None):
    if not options:
        options = {}
    rre=re.compile('-gcc\d+-mt')
    c_d = options.get("location", '.') + "/lib"
    files = [(os.path.join(c_d, i), os.path.join(c_d, rre.sub('', i)))
             for i in os.listdir(c_d)
             if (i.endswith('mt.so')
                 and os.path.isfile(
                     os.path.join(c_d, i)
                 )
                )
            ]
    for f in files:
        try:
            os.symlink(f[0], f[1])
        except:
            pass
    fp = os.path.join(buildout['buildout']['directory'], 'user-config.jam')
    if os.path.exists(fp):
        os.remove(fp)
    relink(options, buildout)

if __name__ == '__main__':
    hook()



# vim:set et sts=4 ts=4 tw=80:
