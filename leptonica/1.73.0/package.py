# -*- coding: utf-8 -*-

name = 'leptonica'

version = '1.73.0'

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')
    env.PATH.append('{root}/bin')
    if building:
        env.LIBLEPT_HEADERSDIR.set('{root}/include')

timestamp = 1610547031

format_version = 2
