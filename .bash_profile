# /etc/skel/.bash_profile

# This file is sourced by bash for login shells.  The following line
# runs your .bashrc and is recommended by the bash info pages.

export PATH="$(du $HOME/.mpu/packages/usr/bin | cut -f2 | tr '\n' ':')$PATH"

if [[ -f ~/.bashrc ]] ; then
	. ~/.bashrc
fi
