# -*- coding: utf-8 -*-

name = 'png'

version = '1.6.29'

build_requires = ['cmake']

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib64')
    # env.PKG_CONFIG_PATH.append('{root}/lib64/pkgconfig')
    if building:
        env.CMAKE_MODULE_PATH.append('{root}/cmake')

timestamp = 1588123921

format_version = 2
