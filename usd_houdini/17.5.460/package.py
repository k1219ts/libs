# -*- coding: utf-8 -*-

name = 'usd_houdini'

version = '17.5.460'

requires = ['DXUSD-1.0']

variants = [['houdini-17.5.460']]

def commands():
    env.USD_ROOT.set('{root}')
    env.HOUDINI_PATH.append('{root}')
    env.HOUDINI_DSO_ERROR.set('1')
    env.HOUDINI_DSO_PATH.append('{root}/dso')
    env.HOUDINI_SCRIPT_PATH.append('{root}/scripts')
    env.HOUDINI_OTLSCAN_PATH.append('{root}/otls')
    env.PYTHONPATH.append('{root}/scripts')

timestamp = 1589186372

format_version = 2
