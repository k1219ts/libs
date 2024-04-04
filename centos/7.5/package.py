# -*- coding: utf-8 -*-

name = 'centos'

version = '7.5'

requires = [
]

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PATH.append('{root}/bin')