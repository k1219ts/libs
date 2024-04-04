# -*- coding: utf-8 -*-

name = 'alembic'

version = '1.7.1'

requires = [
    'hdf5-1.10.0',
    'ilmbase-2.2.0',
    'openexr-2.2.0'
]

build_requires = [
    'gcc-6.3.1',
    'cmake'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')

timestamp = 1588742034

format_version = 2
