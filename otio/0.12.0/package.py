# -*- coding: utf-8 -*-

name = 'otio'

version = '0.12.0'

tools = [
    'otiocat',
    'otioconvert',
    'otiostat',
    'otioview'
]

requires = ['pyside2']

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PATH.prepend('{root}/bin')
    env.PYTHONPATH.prepend('{root}/lib/python2.7/site-packages')

    # Pipeline scripts
    env.BACKSTAGE_OTIO_PATH.set('/backstage/apps/OTIO')
    env.OTIO_SCRIPT_PATH.set('{}/scripts'.format(env.BACKSTAGE_OTIO_PATH))
    env.OTIO_NAUTILUS_SCRIPT_PATH.set('{}/shares/nautilus'.format(env.BACKSTAGE_OTIO_PATH))

timestamp = 1589175578

format_version = 2
