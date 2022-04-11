#!/bin/bash

SNAME=$0
SELECTION=$1 

export CONDA_ACTIVATE=/APSshare/miniconda/x86_64/bin/activate
#export CONDA_ENVIRONMENT=bluesky_2021_1
export CONDA_ENVIRONMENT=bluesky_2021_2
# bluesky

export IPYTHON_PROFILE=bluesky
export IPYTHONDIR=/home/beams2/MWYMAN/.ipython-bluesky

source ${CONDA_ACTIVATE} ${CONDA_ENVIRONMENT}

start_console() {
	export CONSOLE_OPTIONS=""
	export CONSOLE_OPTIONS="${CONSOLE_OPTIONS} --profile=${IPYTHON_PROFILE}"
	export CONSOLE_OPTIONS="${CONSOLE_OPTIONS} --ipython-dir=${IPYTHONDIR}"
	export CONSOLE_OPTIONS="${CONSOLE_OPTIONS} --IPCompleter.use_jedi=False"
	export CONSOLE_OPTIONS="${CONSOLE_OPTIONS} --InteractiveShellApp.hide_initial_ns=False"
	ipython ${CONSOLE_OPTIONS}
}

start_jupyter() {
#	export JUPYTER_CONFIG_DIR=${IPYTHONDIR}/profile_bluesky/startup
	export JUPYTER_CONFIG_DIR=${IPYTHONDIR}
	jupyter lab
}

case ${SELECTION} in
	lab)
	    start_jupyter
	    ;;
	    
	console)
		start_console
		;;
		
	*)
		echo " "
		echo "Usage:"
		echo "blueskyRavioli.sh [lab|console]"
		echo " "
		;;
esac
