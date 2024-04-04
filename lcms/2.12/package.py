# -*- coding: utf-8 -*-

name = 'lcms'

version = '2.12'

build_requires = [
    'gcc-6.3.1',
    'cmake'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')

timestamp = 1615099408

format_version = 2
