#!/bin/bash

FILE=~/.zshrc    
if [ -f $FILE ]; then
   mv $FILE $FILE.bak
fi

PWD=$(pwd)
ln -sf $PWD/zshrc ~/.zshrc
ln -sf $PWD/tball_custom_zsh ~/.tball_custom_zsh


ANTIGEN=~/antigen/antigen.zsh
if [ ! -f $ANTIGEN ]; then
   	PARENTDIR="$(dirname "$ANTIGEN")"
	mkdir $PARENTDIR
	curl -L git.io/antigen > $ANTIGEN
fi


