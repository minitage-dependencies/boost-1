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
import os

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

if __name__ == '__main__':
    hook()



# vim:set et sts=4 ts=4 tw=80:
