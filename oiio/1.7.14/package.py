# -*- coding: utf-8 -*-

name = 'oiio'

version = '1.7.14'

requires = [
    'openexr-2.2.0',
    'ocio-1.1.0',
    'jpeg-1.5.3',
    'png-1.6.29',
    'tiff-4.1.0',
    'zlib-1.2.11',
    'boost-1.61.0'
]

build_requires = ['gcc-6.3.1']

def commands():
    env.PATH.prepend('{root}/bin')
    env.LD_LIBRARY_PATH.append('{root}/lib')
    if building:
        env.CMAKE_MODULE_PATH.append('{root}/cmake')

timestamp = 1588746770

format_version = 2
