import sys
import os
import utils

utils.build_tcl()
utils.build_zlib()
utils.build_libpng()
utils.build_freetype()

if 'LIB' in os.environ:
    os.environ['LIB'] = '{};{}'.format(os.environ['LIB'], utils.config_dir())
else:
    os.environ['LIB'] = utils.config_dir()

os.environ['LIB'] = '{};{}'.format(os.environ['LIB'], os.path.join(os.path.dirname(sys.executable), 'tcl'))

if 'INCLUDE' in os.environ:
    os.environ['INCLUDE'] = '{};{};{}'.format(os.environ['INCLUDE'], utils.config_dir(), utils.tcl_config_dir())
else:
    os.environ['INCLUDE'] = '{};{}'.format(utils.config_dir(), utils.tcl_config_dir())

# Wouldn't it be nice if related mpl dir could be set on command line?
mydir = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.join(mydir, '..', 'matplotlib'))
# Wouldn't it be nice if 'install' wasn't hard-coded?
os.system('{} setup.py install'.format(sys.executable))
