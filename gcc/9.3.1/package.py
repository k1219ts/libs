name = 'gcc'
version = '9.3.1'

def commands():
    #command("source /opt/rh/devtoolset-9/enable")
    #env.PATH="${PATH}"

    env.PATH.prepend('/opt/rh/devtoolset-9/root/usr/bin')
    env.MANPATH.prepend('/opt/rh/devtoolset-9/root/usr/share/man')
    env.INFOPATH.prepend('/opt/rh/devtoolset-9/root/usr/share/info')
    env.PCP_DIR.prepend('/opt/rh/devtoolset-9/root')

    # after rpm error
    env.LD_LIBRARY_PATH.prepend('/opt/rh/devtoolset-9/root/usr/lib/dyninst')
    env.LD_LIBRARY_PATH.prepend('/opt/rh/devtoolset-9/root/usr/lib64/dyninst')
    env.LD_LIBRARY_PATH.prepend('/opt/rh/devtoolset-9/root/usr/lib')
    env.LD_LIBRARY_PATH.prepend('/opt/rh/devtoolset-9/root/usr/lib64')
    env.PKG_CONFIG_PATH.prepend('/opt/rh/devtoolset-9/root/usr/lib64/pkgconfig')
