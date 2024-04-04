# -*- coding: utf-8 -*-

name = 'ocio'

version = '1.1.0'

requires = ['python-2.7.16']

build_requires = ['gcc-6.3.1']

def commands():
    env.LD_LIBRARY_PATH.prepend('{root}/lib')
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')
    if building:
        env.CMAKE_MODULE_PATH.append('{root}/cmake')

timestamp = 1588746386

format_version = 2
