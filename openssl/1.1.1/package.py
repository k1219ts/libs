# -*- coding: utf-8 -*-

name = 'openssl'

version = '1.1.1'

build_requires = [
#    'gcc-6.3.1',
#    'cmake-3.14'
]

def commands():
    env.PATH.prepend('{root}/bin')
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')

timestamp = 1686797233

format_version = 2
