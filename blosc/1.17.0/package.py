# -*- coding: utf-8 -*-

name = 'blosc'

version = '1.17.0'

build_requires = ['cmake']

def commands():
    env.LD_LIBRARY_PATH.prepend('{root}/lib')

timestamp = 1588154373

format_version = 2
