"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/santhoshse7en/utuby
"""
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

# Always prefer setuptools over distutils
import setuptools

keywords = ['youtube', "comments", "without-api", "youtube_scraper", 'youtube_comments', 'vaderSentiment',
'bs4', 'textblob', 'youtube_sentiment', "sentiment_analysis", 'youtube_analysis', 'lxml', 'ajax']

setuptools.setup(
    name="utuby",
    version="0.5",
    author="M Santhosh Kumar",
    author_email="santhoshse7en@gmail.com",
    description="Python package which to access the YouTube database without API",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/santhoshse7en/utuby",
    keywords = keywords,
    install_requires=['beautifulsoup4', 'pandas', 'vaderSentiment', 'textblob', 'lxml', 'cssselect', 'requests'],
    packages = setuptools.find_packages(),
    classifiers=['Development Status :: 4 - Beta',
              'Intended Audience :: End Users/Desktop',
              'Intended Audience :: Developers',
              'Intended Audience :: System Administrators',
              'License :: OSI Approved :: MIT License',
              'Operating System :: OS Independent',
              'Programming Language :: Python',
              'Topic :: Communications :: Email',
              'Topic :: Office/Business',
              'Topic :: Software Development :: Bug Tracking',
              ],
)
