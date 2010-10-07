import os
import platform

def setenv(options,buildout):
    #os.environ['EXPAT_INCLUDE']=buildout['expat']['location']+'/include'
    #os.environ['EXPAT_LIBPATH']=buildout['expat']['location']+'/lib' 
    #os.environ['BZIP2_INCLUDE'] = buildout['bz2']['location'] + "/include"
    #os.environ['BZIP2_LIBPATH'] = buildout['bz2']['location'] + "/lib"
    ## cf http://www.boost.org/doc/libs/1_38_0/libs/iostreams/doc/installation.html
    #os.environ['ZLIB_INCLUDE'] = buildout['zlib']['location'] + "/include"
    #os.environ['ZLIB_LIBPATH'] = buildout['zlib']['location'] + "/lib"
    os.environ['ICU_ROOT'] = buildout['icu']['location']
    os.environ['ICU_PATH']= os.environ['ICU_ROOT'] 
    compiler = 'gcc'
    if 'darwin' in platform.uname()[0].lower():
        compiler = 'darwin'
    datas = {
        'compiler': compiler,
        'LDFLAGS': os.environ['LDFLAGS'],
        'CXXFLAGS': os.environ['CXXFLAGS'],
        'CFLAGS': os.environ['CFLAGS'],
    }
    flags="""
using %(compiler)s : : : <compileflags>"%(CFLAGS)s" <linkflags>"%(LDFLAGS)s" ;
using mpi ;
""" % datas
    fp = os.path.join(buildout['buildout']['directory'], 'user-config.jam')
    fd = open(fp, 'w')
    fd.write(flags)
    fd.flush()
    fd.close()
# vim:set ts=4 sts=4 et  :
