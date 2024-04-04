# -*- coding: utf-8 -*-

name = 'otio'

version = '0.13.2'

tools = [
    'otiocat',
    'otioconvert',
    'otiostat',
    'otioview'
]

# requires = ['pyside2']

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PATH.prepend('{root}/bin')
    env.PYTHONPATH.prepend('{root}/lib/python2.7/site-packages')

timestamp = 1605150472

format_version = 2
