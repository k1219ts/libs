# -*- coding: utf-8 -*-

name = 'yaml'

version = '0.6.3'

requires = []

build_requires = [
    'gcc-6.3.1',
    'cmake'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')

timestamp = 1615098968

format_version = 2
