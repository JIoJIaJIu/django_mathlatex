#!/usr/bin/env python
from distutils.core import setup

setup(
    name='django_mathlatex',
    version='0.1.0',
    author='emesik',
    url='https://github.com/emesik/django_mathlatex',
    packages=['django_mathlatex'],
    requires=[
        'latex',
        'dvipng',
    ],
)
