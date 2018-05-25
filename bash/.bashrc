# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac



# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

alias fernie="ssh fernando@LXFCAMPOS01"

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# some more ls aliases
alias ll='ls -lhF'
alias la='ls -A'
alias l='ls -CF'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

## Setup an interactive Prompt

GREEN="\[\e[0;32m\]"
BLUE="\[\e[0;34m\]"
RED="\[\e[0;31m\]"
BRED="\e[1;31m\]"
YELLOW="\[\e[0;33m\]"
WHITE="\e[0;37m\]"
BWHITE="\e[1;37m\]"
COLOREND="\[\e[00m\]"

# Responsive Prompt
root_name(){
	if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    		debian_chroot=$(cat /etc/debian_chroot)
	fi
	
	echo -e "${debian_chroot:+($debian_chroot)}${BLUE}\u@\h${COLOREND}"
}



working_directory() {
	dir=`pwd`
	in_home=0
	if [[ `pwd` =~ ^"$HOME"(/|$) ]]; then
		dir="~${dir#$HOME}"
		in_home=1
	fi

	workingdir=""
	if [[ `tput cols` -lt 110 ]]; then
		first="/`echo $dir | cut -d / -f 2`"
		letter=${first:0:2}
		if [[ $in_home == 1 ]]; then
			letter="~$letter"
		fi
		proj=`echo $dir | cut -d / -f 3`
		beginning="$letter/$proj"
		end=`echo "$dir" | rev | cut -d / -f1 | rev`

		if [[ $proj == "" ]]; then
			workingdir="$dir"
		elif [[ $proj == "~" ]]; then
			workingdir="$dir"
		elif [[ $dir =~ "$first/$proj"$ ]]; then
			workingdir="$beginning"
		elif [[ $dir =~ "$first/$proj/$end"$ ]]; then
			workingdir="$beginning/$end"
		else
			workingdir="$beginning/.../$end"
		fi
	else
		workingdir="$dir"
	fi

	echo -e "${GREEN}$workingdir${COLOREND}"
}

parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

prompt() {
	if [[ $? -eq 0 ]]; then
		exit_status="${BLUE}▸${COLOREND} "
	else
		exit_status="${RED}▸${COLOREND} "
	fi

	GIT_BRANCH="${YELLOW}$(parse_git_branch)${COLOREND}"

	PS1="\n$(root_name) $(working_directory)$GIT_BRANCH\n$exit_status"
}



PROMPT_COMMAND=prompt


# Add some useful directory commands
function up( )
{
LIMIT=$1
P=$PWD
for ((i=1; i <= LIMIT; i++))
do
    P=$P/..
done
cd $P
export MPWD=$P
}

function back( )
{
LIMIT=$1
P=$MPWD
for ((i=1; i <= LIMIT; i++))
do
    P=${P%/..}
done
cd $P
export MPWD=$P
}



export PATH="/opt/timesys/toolchains/toolchain-arm_v5te_gcc-4.6-linaro_uClibc-0.9.33.2_eabi/bin:$PATH"
export PATH="/opt/timesys/toolchains/toolchain-arm_v5te_gcc-4.6-linaro_uClibc-0.9.33.2_eabi/lib:$PATH"
export PATH="/usr/local/arm-linux-4.4.2/bin:$PATH"
export PATH=$PATH:/usr/local/go/bin

export PATH=$PATH:/usr/local/scripts
export ZTR_SDK_HOME=/home/tballast/SSID/ZTRSDK/trunk
export MANPATH="/usr/local/arm-linux-4.4.2/man:$MANPATH"

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/tballast/SSID/ZTRSDK/trunk/lib/boost/1.59.0/lib/x64:/home/tballast/SSID/ZTRSDK/trunk/lib/libnodave/0.8.4.6/lib/x64:/opt/ztr/lib
source /home/tballast/SSID/TOOLS/Docker/dockMaster.sh


#git function used to silently hook into git clone call and force use of templated hooks
function git {
    if [[ $1 = "clone" && $PWD =~ /home/tballast/GIT ]]; then
        /usr/bin/git clone --template=$HOME/.git-templates ${@:2}
    else
        /usr/bin/git "$@"
    fi
}


#function make {
#    /usr/bin/make $@ 2>&1 | grep -E --color=auto 'error|$'
#}

function make {
/usr/bin/make $@ 2>&1 | sed -e 's/\(.*note:.*\)/\o033[38;5;82m\1\o033[39m/' -e 's/\(.*warning.*\)/\o033[1m\o033[38;5;172m\1\o033[39m\o033[21m/' -e 's/\(.*: error:.*\)/\o033[1m\o033[31m\1\o033[39m\o033[21m/' -e 's/\(.* Error .*\)/\o033[31m\1\o033[39m/' -e 's/\(.*In file included .*\)/\o033[38;5;165m\1\o033[39m/' -e 's/\(.*: In .*\)/\o033[38;5;165m\1\o033[39m/' -e 's/\(.*                 from .*\)/\o033[38;5;165m\1\o033[39m/' -e 's/\(.*: fatal error:.*\)/\o033[1m\o033[31m\1\o033[39m\o033[21m/';
}
