# -*- coding: utf-8 -*-

name = 'pybind11'

version = '2.6.1'

build_requires = [
    'gcc-6.3.1',
    'cmake',
    'python-2.7'
]

def commands():
    env.CMAKE_MODULE_PATH.prepend('{root}/share/cmake/pybind11')
    env.PYBIND11_INCLUDE_PATH.set('{root}/include')

timestamp = 1615098015

format_version = 2
