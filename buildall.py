import sys
import os
import shutil
import utils
import optparse


def main(options):
    if not options.no_tcl:
        utils.build_tcl()
    utils.build_zlib()
    utils.build_libpng()
    utils.build_freetype()

    shutil.copy(os.path.join(utils.DEPSSRC, 'stdint.h'), os.path.join(utils.config_dir(), 'stdint.h'))

    if 'LIB' in os.environ:
        os.environ['LIB'] = '{};{}'.format(os.environ['LIB'], utils.config_dir())
    else:
        os.environ['LIB'] = utils.config_dir()

    os.environ['LIB'] = '{};{}'.format(os.environ['LIB'], os.path.join(os.path.dirname(sys.executable), 'tcl'))

    if 'INCLUDE' in os.environ:
        os.environ['INCLUDE'] = '{};{};{}'.format(os.environ['INCLUDE'], utils.config_dir(), utils.tcl_config_dir())
    else:
        os.environ['INCLUDE'] = '{};{}'.format(utils.config_dir(), utils.tcl_config_dir())

    os.chdir(options.mpl_dir)

    if options.use_pip:
        os.system('pip install -e .')
    else:
        os.system('{} setup.py {}'.format(sys.executable, options.setup_cmd))


if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('--use_pip', '-p', action="store_true", dest="use_pip",
                                          default=False, help="Whether to use `pip install -e .`")
    mydir = os.path.dirname(os.path.abspath(__file__))
    default_path = os.path.join(mydir, '..', 'matplotlib')
    parser.add_option('--mpl_dir', '-d', action="store", dest="mpl_dir",
                                          default=default_path, help="Matplotlib repo directory")
    parser.add_option('--setup_cmd', '-s', action="store", dest="setup_cmd",
                                           default="install", help="Command to pass to setup.py")
    parser.add_option('--no_tcl', '-n', action="store_true", dest="no_tcl",
                                          default=False, help="Don't build Tcl/Tk (for headless MPL servers)")
    options, rem = parser.parse_args()

    main(options)
