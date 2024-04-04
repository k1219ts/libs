name = 'freetype'
version = '2.8-14'

def commands():
    env.LD_LIBRARY_PATH.prepend('{root}/lib64')
    env.PKG_CONFIG_PATH.prepend('{root}/lib64/pkgconfig')

