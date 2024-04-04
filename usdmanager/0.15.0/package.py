# -*- coding: utf-8 -*-

name = 'usdmanager'

version = '0.15.0'

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

timestamp = 1693366715

format_version = 2
