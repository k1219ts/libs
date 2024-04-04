# -*- coding: utf-8 -*-

name = 'otio'

version = '0.14.0'

tools = [
    'otiocat',
    'otioconvert',
    'otiostat',
    'otioview'
]

build_requires = [
    'python-2.7',
    'cmake',
    'pyside2'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PATH.prepend('{root}/bin')
    env.PYTHONPATH.prepend('{root}/lib/python2.7/site-packages')

timestamp = 1614733114

format_version = 2
