name = 'gcc'
version = '6.3.1'

def commands():
    #command("source /opt/rh/devtoolset-6/enable")
    #env.PATH="${PATH}"

    env.PATH.prepend('/opt/rh/devtoolset-6/root/usr/bin')
    env.MANPATH.prepend('/opt/rh/devtoolset-6/root/usr/share/man')
    env.INFOPATH.prepend('/opt/rh/devtoolset-6/root/usr/share/info')
    env.PCP_DIR.prepend('/opt/rh/devtoolset-6/root')
    env.PERL5LIB.prepend('/opt/rh/devtoolset-6/root/usr/lib64/perl5/vendor_perl:/opt/rh/devtoolset-6/root/usr/lib/perl5:/opt/rh/devtoolset-6/root/usr/share/perl5/vendor_perl')

    # after rpm error
    env.LD_LIBRARY_PATH.prepend('/opt/rh/devtoolset-6/root/usr/lib')
    env.LD_LIBRARY_PATH.prepend('/opt/rh/devtoolset-6/root/usr/lib64')
    env.pythonvers.set('2.7')
    env.PYTHONPATH.prepend('/opt/rh/devtoolset-6/root/usr/lib/python2.7/site-packages')
    env.PYTHONPATH.prepend('/opt/rh/devtoolset-6/root/usr/lib64/python2.7/site-packages')
