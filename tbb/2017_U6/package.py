# -*- coding: utf-8 -*-

name = 'tbb'

version = '2017_U6'

variants = [
    ['gcc-4.8.5'],
    ['gcc-6.3.1']
]

def commands():
    if building:
        env.CMAKE_MODULE_PATH.append('{root}/cmake')
        env.TBB_DIR.set('{root}')

timestamp = 1588177409

format_version = 2
