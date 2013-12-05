matplotlib-winbuild
===================

This is a set of scripts to build matplotlib from source on the MS Windows
platform.  It includes building of the various dependencies.

The build goes like this:

	REM clone the matplotlib-winbuild github
	build_dep.cmd
	build_mpl.cmd
