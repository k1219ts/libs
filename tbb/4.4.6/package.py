# -*- coding: utf-8 -*-

name = 'tbb'

version = '4.4.6'

variants = [
    ['gcc-4.8.5'],
    ['gcc-6.3.1']
]

def commands():
    if building:
        env.CMAKE_MODULE_PATH.append('{root}/cmake')

timestamp = 1588177621

format_version = 2
