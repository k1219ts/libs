
#ifndef SEEXPR2_EXPORT_H
#define SEEXPR2_EXPORT_H

#ifdef SEEXPR2_STATIC_DEFINE
#  define SEEXPR2_EXPORT
#  define SEEXPR2_NO_EXPORT
#else
#  ifndef SEEXPR2_EXPORT
#    ifdef SeExpr2_EXPORTS
        /* We are building this library */
#      define SEEXPR2_EXPORT __attribute__((visibility("default")))
#    else
        /* We are using this library */
#      define SEEXPR2_EXPORT __attribute__((visibility("default")))
#    endif
#  endif

#  ifndef SEEXPR2_NO_EXPORT
#    define SEEXPR2_NO_EXPORT __attribute__((visibility("hidden")))
#  endif
#endif

#ifndef SEEXPR2_DEPRECATED
#  define SEEXPR2_DEPRECATED __attribute__ ((__deprecated__))
#endif

#ifndef SEEXPR2_DEPRECATED_EXPORT
#  define SEEXPR2_DEPRECATED_EXPORT SEEXPR2_EXPORT SEEXPR2_DEPRECATED
#endif

#ifndef SEEXPR2_DEPRECATED_NO_EXPORT
#  define SEEXPR2_DEPRECATED_NO_EXPORT SEEXPR2_NO_EXPORT SEEXPR2_DEPRECATED
#endif

#if 0 /* DEFINE_NO_DEPRECATED */
#  ifndef SEEXPR2_NO_DEPRECATED
#    define SEEXPR2_NO_DEPRECATED
#  endif
#endif

#endif /* SEEXPR2_EXPORT_H */
