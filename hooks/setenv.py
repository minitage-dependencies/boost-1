import os

def setenv(options,buildout):
    os.environ['EXPAT_INCLUDE']=buildout['expat']['location']+'/include'
    os.environ['EXPAT_LIBPATH']=buildout['expat']['location']+'/lib'
    os.environ['ICU_ROOT'] = buildout['icu']['location']
    os.environ['ICU_PATH']= os.environ['ICU_ROOT']
    os.environ['BZIP2_INCLUDE'] = buildout['bz2']['location'] + "/include"
    os.environ['BZIP2_LIBPATH'] = buildout['bz2']['location'] + "/lib"
    # cf http://www.boost.org/doc/libs/1_38_0/libs/iostreams/doc/installation.html
    os.environ['ZLIB_INCLUDE'] = buildout['zlib']['location'] + "/include"
    #os.environ['ZLIB_SOURCE'] = buildout['zlib']['location'] + "/include"
    os.environ['ZLIB_LIBPATH'] = buildout['zlib']['location'] + "/lib"

    os.environ['CFLAGS']   = os.environ.get('CFLAGS',"")\
    + "-I %s/include" % buildout['bz2']['location'] \
    + "-I %s/include" % buildout['zlib']['location']

    os.environ['CPPFLAGS'] = os.environ.get('CFLAGS',"")
    os.environ['CXXFLAGS'] = os.environ.get('CFLAGS',"")
    os.environ['LDFLAGS']  = os.environ.get('LDFLAGS',"") \
    + "-L %s -Wl,-rpath -Wl,%s" %( buildout['zlib']['location'],  buildout['zlib']['location']) \
    + "-L %s -Wl,-rpath -Wl,%s" %( buildout['zlib']['location'],  buildout['zlib']['location'])
# vim:set ts=4 sts=4 et  :
