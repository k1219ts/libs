# -*- coding: utf-8 -*-

name = 'tiff'

version = '4.0.7'

build_requires = ['cmake']

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib64')
    # env.PKG_CONFIG_PATH.append('{root}/lib64/pkgconfig')
    if building:
        env.CMAKE_MODULE_PATH.append('{root}/cmake')

timestamp = 1588126009

format_version = 2
