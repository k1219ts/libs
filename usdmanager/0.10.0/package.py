# -*- coding: utf-8 -*-

name = 'usdmanager'

version = '0.10.0'

build_requires = ['python-2.7']

requires = [
    'python-2.7',
    'pyside2',
    'usdtoolkit',
]

tools = [
    'usdmanager'
]

def commands():
    env.PATH.append('{root}/bin')
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')

timestamp = 1588908310

format_version = 2
