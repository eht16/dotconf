HISTFILE=~/.zsh_histfile
HISTSIZE=2000
SAVEHIST=2000
REPORTTIME=2
watch=(notme)               # watch login/logout
bindkey -e
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word

setopt autocd nomatch histignorealldups complete_aliases hist_save_no_dups hist_reduce_blanks hist_expire_dups_first share_history
unsetopt appendhistory beep extendedglob


zstyle :compinstall filename '/home/enrico/.zshrc'
autoload -Uz compinit
compinit


for file in ~/.zsh/*
do
	source $file
done
