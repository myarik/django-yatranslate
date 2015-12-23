#!/usr/bin/env python
from distutils.core import setup

setup(
    name='django-yatranslate',
    version='0.1',
    description='Simple translate',
    author='Yaroslav Muravskiy',
    author_email='y@myarik.com',
    url='http://github.com/myarik/django-yatranslate.git',
    py_modules=['django', 'grab', 'pycurl', 'lxml'],
    packages=['yatranslate', ]
)
