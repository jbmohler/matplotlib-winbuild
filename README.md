matplotlib-winbuild
===================

This is a set of scripts to build matplotlib from source on the MS Windows
platform.  It includes building of the various dependencies.  The origin of
these scripts is the comment by cgohlke in
https://github.com/matplotlib/matplotlib/issues/1717 .

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
