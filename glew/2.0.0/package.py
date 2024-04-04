# -*- coding: utf-8 -*-

name = 'glew'

version = '2.0.0'

build_requires = ['cmake']

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib64')
    # env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig/')
    # env.LD_PRELOAD.append('{root}/lib64/libGLEW.so.2.0')
    if building:
        env.CMAKE_MODULE_PATH.append('{root}/cmake')

timestamp = 1588135886

format_version = 2
