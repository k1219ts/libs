# -*- coding: utf-8 -*-

name = 'ilmbase'

version = '2.3.0'

build_requires = [
    'gcc-6.3.1',
    'cmake'
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')
    if building:
        env.ILMBASE_ROOT.set('{root}')

timestamp = 1615086482

format_version = 2
