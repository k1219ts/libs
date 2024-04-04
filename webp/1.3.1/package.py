# -*- coding: utf-8 -*-

name = 'webp'

version = '1.3.1'

build_requires = [
#    'gcc-9.3.1',
#    'cmake'
]

def commands():
    env.PATH.append('{root}/bin')
    env.LD_LIBRARY_PATH.append('{root}/lib64')
    env.PKG_CONFIG_PATH.append('{root}/lib64/pkgconfig')
    env.CMAKE_PREFIX_PATH.append('{root}/share/WebP/cmake')
    if building:
        env.CMAKE_PREFIX_PATH.append('{root}/share/WebP/cmake')

timestamp = 1688558456

format_version = 2
