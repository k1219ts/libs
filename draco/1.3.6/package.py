# -*- coding: utf-8 -*-

name = 'draco'

version = '1.3.6'

build_requires = [
    'gcc-6.3.1',
    'cmake'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PATH.append('{root}/bin')

timestamp = 1588840859

format_version = 2
