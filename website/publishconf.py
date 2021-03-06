#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://www.mlugs.de'
#RELATIVE_URLS = False

FEED_RSS = "feed/all.rss.xml"
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

DELETE_OUTPUT_DIRECTORY = True
PAGE_PATHS = ['content/pages']

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
