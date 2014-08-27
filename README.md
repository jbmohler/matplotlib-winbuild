Building Matplotlib on Windows
==============================

This is a set of scripts to build matplotlib from source on the MS Windows
platform.  It builds matplotlib requiring only Visual Studio and CMake as
pre-requisites; other library dependencies are embedded in this repository.
Any complicated or other dependencies are considered bugs in this build script.

The Python shipped from http://www.python.org is compiled with Visual Studio
2008 for versions before 3.3 and Visual Studio 2010 for 3.3 and later.  Python
extensions are recommended to be compiled with the same compiler.  These
scripts and the matplotlib `setup.py` look for the correct version via
distutils.  The .NET Framework 4.0 is required for MSBuild, but you likely
already have it.

In addition to Visual Studio [CMake](http://www.cmake.org) is required for
building libpng.  For building documentation, you will need to install numpydoc
and miktex.  The required freetype, zlib, libpng, tcl, & tk source code is
bundled with this repository since there is no canonical Windows package manager.

To build & install matplotlib in your Python, do:

	git clone https://github.com/matplotlib/matplotlib
	git clone https://github.com/jbmohler/matplotlib-winbuild
	python matplotlib-winbuild\buildall.py

The build script will auto-detect Python version & 32/64 bit automatically.

The origin of these scripts is the comment by cgohlke in
https://github.com/matplotlib/matplotlib/issues/1717 .
