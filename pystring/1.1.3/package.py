# -*- coding: utf-8 -*-

name = 'pystring'

version = '1.1.3'

build_requires = [
    'gcc-6.3.1',
    'cmake'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')

timestamp = 1615098432

format_version = 2
