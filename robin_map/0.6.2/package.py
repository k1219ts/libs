# -*- coding: utf-8 -*-

name = 'robin_map'

version = '0.6.2'

build_requires = [
    'gcc-6.3.1',
    'cmake'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib64')

timestamp = 1595203065

format_version = 2
