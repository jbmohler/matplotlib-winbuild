Building Matplotlib on Windows
==============================

This is a set of scripts to build matplotlib from source on the MS Windows
platform.  It includes building of the various dependencies.  The origin of
these scripts is the comment by cgohlke in
https://github.com/matplotlib/matplotlib/issues/1717 .

The Python shipped from http://www.python.org is compiled with Visual Studio
2008 for versions before 3.3 and Visual Studio 2010 for 3.3 and later.
Python extensions are recommended to be compiled with the same compiler.  The
matplotlib `setup.py` looks for the correct version via distutils.  The .NET
Framework 4.0 is required for MSBuild, but you likely already have it.

In addition to Visual Studio, `CMake <http://www.cmake.org>`_ is required for
building libpng.  For building documentation, you will need to install numpydoc
and miktex.  The required freetype, zlib, libpng, tcl, & tk source code is
bundled with matplotlib since there is no canonical Windows package manager.

Instructions as above will build and install in the Python installation used to
launch `setup.py`.  Alternatively to build an installation binary that can be
used on other Windows machines with a matching Python, run::

  python setup.py bdist_wininst

The build goes like this:

	REM clone the matplotlib-winbuild github
	REM navigate to this directory in a visual studio command prompt
	build_dep.cmd
	git clone https://github.com/matplotlib/matplotlib.git
	build_mpl.cmd

So far I've selected the Python target version in build\_mpl.cmd by commenting
out the versions I wasn't interested in building.  A nice improvement would be
to break up build\_mpl.cmd into scripts for each version or a command line
parameter for selecting a Python version.
