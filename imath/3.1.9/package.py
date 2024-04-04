# -*- coding: utf-8 -*-

name = 'imath'

version = '3.1.9'

build_requires = [
#    'gcc-6.3.1',
    'cmake'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib64')
    if building:
        env.CMAKE_MODULE_PATH.append('{root}/lib64/cmake')

timestamp = 1686913366

format_version = 2
