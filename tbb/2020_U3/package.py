# -*- coding: utf-8 -*-

name = 'tbb'

version = '2020_U3'

variants = [
    ['gcc-4.8.5'],
    ['gcc-6.3.1'],
    ['gcc-9.3.1']
]

def commands():
    if building:
        env.CMAKE_MODULE_PATH.append('{root}/cmake')

timestamp = 1689937889

format_version = 2
