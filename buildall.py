import sys
import os
import buildutils

buildutils.build_tcl()
buildutils.build_zlib()
buildutils.build_libpng()
buildutils.build_freetype()

if 'LIB' in os.environ:
    os.environ['LIB'] = '{};{}'.format(os.environ['LIB'], buildutils.config_dir())
else:
    os.environ['LIB'] = buildutils.config_dir()

os.environ['LIB'] = '{};{}'.format(os.environ['LIB'], os.path.join(os.path.dirname(sys.executable), 'tcl'))

if 'INCLUDE' in os.environ:
    os.environ['INCLUDE'] = '{};{};{}'.format(os.environ['INCLUDE'], buildutils.config_dir(), buildutils.tcl_config_dir())
else:
    os.environ['INCLUDE'] = '{};{}'.format(buildutils.config_dir(), buildutils.tcl_config_dir())

os.chdir('..\\matplotlib')
os.system('{} setup.py install'.format(sys.executable))
