# -*- coding: utf-8 -*-

name = 'opensubdiv'

version = '3.4.3'

#build_requires = ['gcc-6.3.1']

def commands():
    env.PATH.prepend('{root}/bin')
    env.LD_LIBRARY_PATH.prepend('{root}/lib')

timestamp = 1588745218

format_version = 2