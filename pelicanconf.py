#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Benjamin Bouvier'
SITENAME = u'24 hours a day'
#SITEURL = 'https://blog.benj.me'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['blog', 'images']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'

FEED_DOMAIN = SITEURL
FEED_ALL_RSS = 'rss'
#TAG_FEED_RSS = '/tag/%s.rss'

THEME = 'themes/Flex'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Theme specific
SITETITLE=u"24 hours a day"
SITESUBTITLE=u"Benjamin Bouvier's blog"
SITELOGO=u"/images/logo.jpeg"

COPYRIGHT_YEAR=u"2015"
MAIN_MENU=True

# Piwik
PIWIK_URL = 'bnjbvr.alwaysdata.net/piwik'
PIWIK_SITE_ID = 1

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ( #('Flux rss', 'https://blog.benj.me/rss'),
        )

# Social widget
SOCIAL = (('github', 'https://github.com/bnjbvr'),
         ('twitter', 'https://twitter.com/bnjbvr'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
