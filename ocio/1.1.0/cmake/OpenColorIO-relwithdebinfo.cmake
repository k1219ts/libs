#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "OpenColorIO" for configuration "RelWithDebInfo"
set_property(TARGET OpenColorIO APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(OpenColorIO PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELWITHDEBINFO "TINYXML_LIB;YAML_CPP_LIB"
  IMPORTED_LOCATION_RELWITHDEBINFO "/backstage/libs/ocio/1.1.0/lib/libOpenColorIO.so.1.1.0"
  IMPORTED_SONAME_RELWITHDEBINFO "libOpenColorIO.so.1"
  )

list(APPEND _IMPORT_CHECK_TARGETS OpenColorIO )
list(APPEND _IMPORT_CHECK_FILES_FOR_OpenColorIO "/backstage/libs/ocio/1.1.0/lib/libOpenColorIO.so.1.1.0" )

# Import target "OpenColorIO_STATIC" for configuration "RelWithDebInfo"
set_property(TARGET OpenColorIO_STATIC APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(OpenColorIO_STATIC PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELWITHDEBINFO "CXX"
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELWITHDEBINFO "TINYXML_LIB;YAML_CPP_LIB"
  IMPORTED_LOCATION_RELWITHDEBINFO "/backstage/libs/ocio/1.1.0/lib/static/libOpenColorIO.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS OpenColorIO_STATIC )
list(APPEND _IMPORT_CHECK_FILES_FOR_OpenColorIO_STATIC "/backstage/libs/ocio/1.1.0/lib/static/libOpenColorIO.a" )

# Import target "ociocheck" for configuration "RelWithDebInfo"
set_property(TARGET ociocheck APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(ociocheck PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "/backstage/libs/ocio/1.1.0/bin/ociocheck"
  )

list(APPEND _IMPORT_CHECK_TARGETS ociocheck )
list(APPEND _IMPORT_CHECK_FILES_FOR_ociocheck "/backstage/libs/ocio/1.1.0/bin/ociocheck" )

# Import target "ociobakelut" for configuration "RelWithDebInfo"
set_property(TARGET ociobakelut APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(ociobakelut PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "/backstage/libs/ocio/1.1.0/bin/ociobakelut"
  )

list(APPEND _IMPORT_CHECK_TARGETS ociobakelut )
list(APPEND _IMPORT_CHECK_FILES_FOR_ociobakelut "/backstage/libs/ocio/1.1.0/bin/ociobakelut" )

# Import target "PyOpenColorIO" for configuration "RelWithDebInfo"
set_property(TARGET PyOpenColorIO APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(PyOpenColorIO PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "/backstage/libs/ocio/1.1.0/lib/python2.7/site-packages/PyOpenColorIO.so"
  IMPORTED_SONAME_RELWITHDEBINFO "PyOpenColorIO.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS PyOpenColorIO )
list(APPEND _IMPORT_CHECK_FILES_FOR_PyOpenColorIO "/backstage/libs/ocio/1.1.0/lib/python2.7/site-packages/PyOpenColorIO.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
