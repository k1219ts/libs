# -*- coding: utf-8 -*-

name = 'centos'

version = '8.5'

requires = [
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PATH.append('{root}/bin')
    env.LD_PRELOAD.prepend('/lib64/libfreetype.so.6')
