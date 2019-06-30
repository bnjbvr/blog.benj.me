#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Benjamin Bouvier'
SITENAME = u"Benjamin Bouvier's blog"
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['blog', 'images']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'

THEME = 'themes/modern'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'fr'

# Theme specific
SITETITLE=u"Benjamin Bouvier"
SITELOGO=u"/images/logo.jpeg"

COPYRIGHT_YEAR=u"2015"
MAIN_MENU=True

LINKS = (
    ('About', 'https://benj.me'),
    ("Slides", 'https://bnjbvr.github.io/slides'),
)

SOCIAL = (
     ('github', 'https://github.com/bnjbvr'),
     ('gitlab', 'https://framagit.org/bnjbvr'),
     ('twitter', 'https://twitter.com/bnjbvr'),
     ('linkedin', 'https://www.linkedin.com/in/bnjbvr'),
)

# Fathom
FATHOM_URL = '1984.b.delire.party'
FATHOM_SITE_ID = 'CSQLE'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

FEED_DOMAIN = SITEURL
FEED_ALL_RSS = u'rss'
TAG_FEED_RSS = u'tag/{slug}.rss'

DEFAULT_PAGINATION = False

JINJA_ENVIRONMENT = {'extensions': []}

PLUGINS = ['minchin.pelican.plugins.post_stats']

ISSO_BASE_URL = 'https://saywhat.benj.me'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
