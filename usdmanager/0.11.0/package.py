# -*- coding: utf-8 -*-

name = 'usdmanager'

version = '0.11.0'

tools = ['usdmanager']

requires = [
    'python-2.7',
    'pyside2',
    'usdtoolkit'
]

build_requires = ['python-2.7']

def commands():
    env.PATH.append('{root}/bin')
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')

timestamp = 1614293019

format_version = 2
