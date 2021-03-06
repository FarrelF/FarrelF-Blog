#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from publishconf import *

THEME = "Flex"  # Menentukan Nama tema yang terinstall melalui pelican-themes, untuk keperluan pengembangan
ROBOTS = 'noindex, nofollow, noarchive, nosnippets'

# Meng-hapus berkas yang tidak terpakai
STATIC_PATHS.remove('extras/robots_for_origin.txt')
del EXTRA_PATH_METADATA['extras/robots_for_origin.txt']
STATIC_PATHS.remove('extras/robots_for_cdn.txt')
del EXTRA_PATH_METADATA['extras/robots_for_cdn.txt']
STATIC_PATHS.remove('extras/robots_for_images.txt')
del EXTRA_PATH_METADATA['extras/robots_for_images.txt']
STATIC_PATHS.remove('extras/ads.txt')
del EXTRA_PATH_METADATA['extras/ads.txt']

# Membuat berkas 'robots.txt' lagi, agar para robot tidak meng-'crawl' Blog Pratinjau
f = open("robots.txt","w+")
f.write("User-Agent: *\r\n")
f.write("Disallow: /\r\n")
f.close()

# Google
GOOGLE_ANALYTICS = ""
GOOGLE_ADSENSE = ''
