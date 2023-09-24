#!/bin/bash

REQUIREMENTS="jupyter numpy pandas pycodestyle pillow flake8 matplotlib"

function when_conda_exist {
	# check and install 42AI environement
	printf "Checking base environment: "
	if conda info --envs | grep -iqF 42AI-$USER; then
		printf "\e[33mDONE\e[0m\n"
	else
		printf "\e[31mKO\e[0m\n"
		printf "\e[33mCreating base environnment:\e[0m\n"
		conda update -n base -c defaults conda -y
		conda create --name 42AI-$USER python=3.11.5 $REQUIREMENTS -y
	fi
}

function set_conda {
	ANACONDA_PATH="/home/$USER/anaconda3"
	CONDA=$ANACONDA_PATH"/bin/anaconda"
	PYTHON_PATH=$(which python)
	MY_SHELL="zsh"
	SCRIPT="Anaconda3-2023.07-2-Linux-x86_64.sh"
	DL_LINK="https://repo.anaconda.com/archive/"$SCRIPT
	DL_LOCATION="/tmp/"
	printf "Checking conda: "
	TEST=$(conda -h 2>/dev/null)
	# $? = 0 if last command (TEST) executed succesfully
	if [ $? == 0 ] ; then
		printf "\e[32mOK\e[0m\n"
		when_conda_exist
		return
	fi
	printf "\e[31mKO\e[0m\n"
	if [ ! -f $DL_LOCATION$SCRIPT ]; then
		printf "\e[33mDonwloading installer:\e[0m\n"
		cd $DL_LOCATION
		curl -LO $DL_LINK
		cd -
	fi
	printf "\e[33mInstalling conda:\e[0m\n"
	bash $DL_LOCATION$SCRIPT -b -p $ANACONDA_PATH
	printf "\e[33mConda initial setup:\e[0m\n"
	$CONDA init $MY_SHELL
	$CONDA config --set auto_activate_base false
	printf "\e[33mCreating 42AI-$USER environnment:\e[0m\n"
	$CONDA update -n base -c defaults conda -y
	$CONDA create --name 42AI-$USER python=3.11.5 $REQUIREMENTS -y
	printf "\e[33mLaunch the following command or restart your shell:\e[0m\n"
	if [ $MY_SHELL == "zsh" ]; then
		printf "\tsource ~/.zshrc\n"
	else
		printf "\tsource ~/.bash_profile\n"
	fi
}

set_conda
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6
