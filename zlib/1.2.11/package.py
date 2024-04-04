# -*- coding: utf-8 -*-

name = 'zlib'

version = '1.2.11'

build_requires = ['cmake']

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    if building:
        env.ZLIB_ROOT.set('{root}')
        env.CMAKE_MODULE_PATH.append('{root}/cmake')

timestamp = 1588129775

format_version = 2
