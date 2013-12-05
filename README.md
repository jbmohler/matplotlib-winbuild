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
