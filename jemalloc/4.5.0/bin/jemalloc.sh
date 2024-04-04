#!/bin/sh

prefix=/backstage/libs/jemalloc/4.5.0
exec_prefix=/backstage/libs/jemalloc/4.5.0
libdir=${exec_prefix}/lib

LD_PRELOAD=${libdir}/libjemalloc.so.2
export LD_PRELOAD
exec "$@"
