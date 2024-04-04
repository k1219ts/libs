# -*- coding: utf-8 -*-

name = 'hdf5'

version = '1.10.0'

build_requires = [
    'gcc-6.3.1',
    'cmake'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')

timestamp = 1588734873

format_version = 2
