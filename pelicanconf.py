#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Benjamin Bouvier'
SITENAME = u'24 hours a day'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['blog', 'images']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'

THEME = 'themes/Flex'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Theme specific
SITETITLE=u"24 hours a day"
SITESUBTITLE=u"Benjamin Bouvier's blog"
SITELOGO=u"/images/logo.jpeg"

COPYRIGHT_YEAR=u"2015"
MAIN_MENU=True

LINKS = ( )
SOCIAL = (('github', 'https://github.com/bnjbvr'),
         ('twitter', 'https://twitter.com/bnjbvr'),
         )

# Piwik
PIWIK_URL = 'bnjbvr.alwaysdata.net/piwik'
PIWIK_SITE_ID = 1

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

FEED_DOMAIN = SITEURL
FEED_ALL_RSS = u'rss'
TAG_FEED_RSS = u'tag/%s.rss'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
