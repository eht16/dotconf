HISTFILE=~/.zsh_histfile
HISTSIZE=2000
SAVEHIST=2000
REPORTTIME=2
watch=(notme)               # watch login/logout
bindkey -e
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word

setopt autocd histignorealldups interactivecomments complete_aliases hist_save_no_dups hist_reduce_blanks hist_expire_dups_first
unsetopt appendhistory beep extendedglob


zstyle :compinstall filename '/home/enrico/.zshrc'
autoload -Uz compinit
compinit

# menu select (http://www.refining-linux.org/archives/40/ZSH-Gem-5-Menu-selection/)
zstyle ':completion:*' menu select

# cool file renaming (http://www.refining-linux.org/archives/36/ZSH-Gem-1-Programmable-file-renaming/)
autoload -U zmv

for file in ~/.zsh/*
do
	source $file
done
