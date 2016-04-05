# reset xterm title
if [ "$PS1" -a "$TERM" != "dumb" ]; then
    xterm_title="Local"
    echo -ne '\033]2;'${xterm_title}'\007'
fi
